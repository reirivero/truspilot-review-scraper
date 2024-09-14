"""
This module contains functions to load review data into CSV files.

Functions:
- load_data: Loads data into a CSV file.
"""

import logging
from src.utils.config import load_config
import pandas as pd

config = load_config()
logging.basicConfig(filename=config['paths']['log_file'], 
                    level=config['logging']['level'], 
                    format=config['logging']['format'])

def load_data(data, output_file):
    """
    Loads data into a CSV file.

    Parameters
    ----------
    data : list
        A list of dictionaries containing the data to be loaded.
    output_file : str
        The name of the output CSV file.

    Returns
    -------
    None
    """
    try:
        df = pd.DataFrame(data)
        df.to_csv(output_file, index=False)
    except Exception as e:
        logging.error(f"Error loading data to {output_file}: {e}")