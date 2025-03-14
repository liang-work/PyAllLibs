import toml
import json
from configparser import  ConfigParser
import os

def load_json(path):
    with open(path,'r',encoding='utf-8') as f:
        return json.load(f)

def load_toml(path):
    with open(path,'r',encoding='utf-8') as f:
        return toml.load(f)

def load_ini(path):
    load = ConfigParser()
    if os.path.exists(path):
        return load.read(path)
    else:
        raise FileNotFoundError(f'"{path}"not found!')