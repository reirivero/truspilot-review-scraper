from src.utils.decorators import handle_http_request, get_time
import logging
from src.utils.config import load_config


config = load_config()
logging.basicConfig(filename=config['paths']['log_file'], 
                    level=config['logging']['level'], 
                    format=config['logging']['format'])
@get_time
@handle_http_request
def get_total_pages(url, soup):
    try:
        pagination = soup.find('nav', {'aria-label': 'Pagination'})
        last_page = pagination.find_all('a')[-2].text.strip()
        return int(last_page)
    except Exception as e:
        logging.error(f"Error getting total pages: {e}")
        return 0
@get_time
@handle_http_request
def extract_reviews(url,soup):
    try:
        return soup.find_all('div', class_='styles_reviewCardInner__EwDq2')
    except Exception as e:
        logging.error(f"Error extracting reviews from URL {url}: {e}")
        return []