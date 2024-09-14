"""
This module contains functions to extract review data from web pages.

Functions:
- get_total_pages: Gets the total number of pages from a given URL.
- extract_reviews: Extracts reviews from a given URL.
"""

from src.utils.decorators import handle_http_request, get_time
import logging
from src.utils.config import load_config


config = load_config()
logging.basicConfig(filename=config['paths']['log_file'], 
                    level=config['logging']['level'], 
                    format=config['logging']['format'])
@get_time
@handle_http_request
def get_total_pages(url: str, soup):
    """
    Gets the total number of pages from a given URL.

    Parameters
    ----------
    url : str
        The URL of the web page.
    soup : BeautifulSoup object
        The BeautifulSoup object containing the HTML content of the page.

    Returns
    -------
    int
        The total number of pages. Returns 0 if an error occurs.
    """
    try:
        pagination = soup.find('nav', {'aria-label': 'Pagination'})
        last_page = pagination.find_all('a')[-2].text.strip()
        return int(last_page)
    except Exception as e:
        logging.error(f"Error getting total pages: {e}")
        return 0
@get_time
@handle_http_request
def extract_reviews(url: str,soup):
    """
    Extracts reviews from a given URL.

    Parameters
    ----------
    url : str
        The URL of the web page.
    soup : BeautifulSoup object
        The BeautifulSoup object containing the HTML content of the page.

    Returns
    -------
    list
        A list of review elements. Returns an empty list if an error occurs.
    """
    try:
        return soup.find_all('div', class_='styles_reviewCardInner__EwDq2')
    except Exception as e:
        logging.error(f"Error extracting reviews from URL {url}: {e}")
        return []