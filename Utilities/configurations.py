import configparser
import os


def get_aut_configurations():
    config = configparser.ConfigParser()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    properties_file_path = os.path.join(current_dir, 'properties.ini')
    config.read(properties_file_path)
    return config
