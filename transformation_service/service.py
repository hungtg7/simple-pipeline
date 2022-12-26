import os

from . import transform_method
from common.config_reader import ConfigReader
from common.file_reader import FileReader


ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DATA_PATH = f"{ROOT_DIR}/storage/raw_data"
MODELLED_DATA_PATH = f"{ROOT_DIR}/storage/modelled_data"
CONFIG_PATH = f"{ROOT_DIR}/configs"


class TransformationService:
    def __init__(self, source_name: str, date: str):
        self.sc_name = source_name
        self.date = date

    def processing_file(self):
        year, month, day = self.date.split("-")
        source_path = f"{RAW_DATA_PATH}/{self.sc_name}/{year}/{month}/{day}"
        modelled_path = f"{MODELLED_DATA_PATH}/" \
                        f"{self.sc_name}/{year}/{month}/{day}"
        config_path = f"{CONFIG_PATH}/{self.sc_name}.yaml"

        config = ConfigReader.read(config_path)
        if not config:
            raise Exception("Config is None")

        df = self.transform(config, source_path)
        self.store(df, modelled_path)

    def transform(self, config, source_path):

        df = FileReader(source_path).read_file()
        if df.empty:
            raise Exception("Df is None")

        if not config.get("transformation_config"):
            raise Exception("Config is missing transformation_config")

        new_cols = []
        for col, conf in config["transformation_config"]["new_schema"].items():
            new_cols.append(col)
            methods = conf.get("transform_method")

            if not methods:
                df[col] = df[conf.get("source_name")]
                continue

            for method in methods:
                func = getattr(transform_method, method["name"])
                sc_name = conf.get("source_name")

                if not sc_name:
                    # Add constant value for a column case
                    df[col] = func(method["param"][0])
                    continue
                elif sc_name == "whole":
                    df[col] = func(df, method.get("param", []))
                    continue

                df[col] = df[sc_name].apply(func, args=method.get("param", []))

        if not new_cols:
            raise Exception("Error not find any new col")

        result_df = df[new_cols]
        # Free mem due to GC reference count
        df = None

        return result_df

    def store(self, df, path):
        os.makedirs(path, exist_ok=True)
        df.to_csv(f"{path}/{self.sc_name}.csv", index=False)
