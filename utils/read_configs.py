import configparser
import os

def read_config_data(category,key):
    config_obj = configparser.RawConfigParser()
    file_path = os.path.join(os.path.dirname(__file__), '..', 'configurations', 'config.ini')
    config_obj = configparser.RawConfigParser()
    config_obj.read(os.path.abspath(file_path))
    return config_obj.get(category, key)