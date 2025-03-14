import toml as toml
import json
from configparser import  ConfigParser

def save_json(path,dicts):
    with open(path,'w',encoding='utf-8') as f:
        return json.dump(f,dicts)

def save_toml(path,dicts):
    with open(path,'w',encoding='utf-8') as f:
        return toml.dump(dicts,f)

def save_ini(path,dicts):
    config = ConfigParser()

    # 将字典转换为configparser可以理解的结构
    for section, options in dicts.items():
        config[section] = options

    # 写入文件
    with open(path, 'w', encoding='utf-8') as configfile:
        config.write(configfile)
