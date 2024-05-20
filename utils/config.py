import configparser

def load_config(config_path):
    config = configparser.ConfigParser()
    config.read(config_path)
    return config

def get_config_value(config, section, option):
    return config.get(section, option)
