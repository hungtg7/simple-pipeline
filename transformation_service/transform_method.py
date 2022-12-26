import pandas
import hashlib
import requests


def get_val_from_dict_by_key(val, key):
    try:
        dict_val = val
        return dict_val.get(key)
    except ValueError:
        return pandas.np.nan


def add_column_constant(val):
    return val


def get_country_code(val):
    try:
        res = requests.get(f"https://api.country.is/{val}")
        print(res)
        if res.status_code != 200:
            return pandas.np.nan
        return res.json()["country"]
    except Exception:
        return pandas.np.nan


def create_primary_key_base_on_col(df, param):
    s = ""
    for p in param:
        s += df[p]

    return s.apply(hash)


def hash(s):
    return int(hashlib.sha1(s.encode("utf-8")).hexdigest(), 16) % (10 ** 8)
