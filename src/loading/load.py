# import json
import logging
from src.utils.config import load_config
import pandas as pd

config = load_config()
logging.basicConfig(filename=config['paths']['log_file'], 
                    level=config['logging']['level'], 
                    format=config['logging']['format'])

def load_data(data, output_file):
    try:
        df = pd.DataFrame(data)
        df.to_csv(output_file, index=False)
    except Exception as e:
        logging.error(f"Error loading data to {output_file}: {e}")