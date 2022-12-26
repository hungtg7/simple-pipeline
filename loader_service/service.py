import os

from sqlalchemy import create_engine

from common.config_reader import ConfigReader
from common.file_reader import FileReader


ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELLED_DATA_PATH = f"{ROOT_DIR}/storage/modelled_data"
CONFIG_PATH = f"{ROOT_DIR}/configs"


class LoaderService:
    def __init__(self, source_name: str, date: str):
        self.engine = create_engine(
            "postgresql://postgres:postgres@postgres/postgres",
            # disable default reset-on-return scheme
            pool_reset_on_return=None,
        )
        self.sc_name = source_name
        self.date = date

    def load(self):
        year, month, day = self.date.split("-")
        modelled_path = f"{MODELLED_DATA_PATH}/" \
                        f"{self.sc_name}/{year}/{month}/{day}"
        config_path = f"{CONFIG_PATH}/{self.sc_name}.yaml"
        config = ConfigReader.read(config_path)

        if not config:
            raise Exception("Config is None")
        pass

        df = FileReader(modelled_path).read_file()
        if df.empty:
            raise Exception("Df is None")

        if not config.get("loader_config"):
            raise Exception("Config is missing loader_config")

        with self.engine.begin() as conn:
            columns = config['loader_config']['schema_info']['columns']
            table_name = config['loader_config']['schema_info']['table']
            pk = config['loader_config']['schema_info']['pk']
            # step 1 - create temporary table and upload DataFrame
            conn.exec_driver_sql(
                f"CREATE TEMPORARY TABLE temp_table AS " \
                f"SELECT * FROM {table_name} " \
                f"WHERE false"
            )
            df.to_sql(
                "temp_table",
                con=conn,
                if_exists='append',
                index=False
            )
            # step 2 - merge temp_table into main_table
            conn.exec_driver_sql(
                f"""\
                INSERT INTO {table_name} ({",".join(columns)})
                SELECT {",".join(columns)} FROM temp_table
                ON CONFLICT ({pk}) DO
                    UPDATE SET
                    {",".join([f'{col} = EXCLUDED.{col}' for col in columns])}
                """
            )
