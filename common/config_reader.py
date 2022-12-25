import yaml


class ConfigReader:
    """
    Object to load config
    """

    def read(path):
        try:
            with open(path) as f:
                config = yaml.load(f, Loader=yaml.FullLoader)
                return config
        except Exception as e:
            raise Exception(f"{e}, Can not open config file")
