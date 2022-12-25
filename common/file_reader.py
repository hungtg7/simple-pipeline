import pandas
import glob


class FileReader:
    def __init__(self, path: str):
        self.file_path = glob.glob(path+"/*")
        if not self.file_path:
            raise Exception(f"path not found: {path}")

        if self.file_path[0].endswith("json"):
            self.file_reader = JsonReader(self.file_path)
        elif self.file_path[0].endswith("csv"):
            self.file_reader = CsvReader(self.file_path)
        else:
            raise Exception(f"FileReader: Not support file type {path} yet")

    def read_file(self):
        return self.file_reader.read_file()


class JsonReader(FileReader):
    """
    Object to read json file to pandas
    """

    def __init__(self, path):
        self.path = path

    def read_file(self):
        dfs = []
        for path in self.path:
            df = pandas.read_json(path, lines=True)
            dfs.append(df)

        df = pandas.concat(dfs)

        return df


class CsvReader(FileReader):
    """
    Object to read csv file to pandas
    """

    def __init__(self, path):
        self.path = path

    def read_file(self):
        dfs = []
        for path in self.path:
            df = pandas.read_csv(path)
            dfs.append(df)

        df = pandas.concat(dfs)

        return df
