"""
This module contains functions to load configuration settings.

Functions:
- load_config: Loads configuration settings from a file.
"""

import yaml
import os

def load_config():
    """
    Loads configuration settings from a YAML file.

    Returns
    -------
    dict
        A dictionary containing the configuration settings.
    """
    config_path=os.path.abspath('./src/utils/config.yaml')
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config