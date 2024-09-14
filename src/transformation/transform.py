"""
This module contains functions to transform review data.

Functions:
- transform_review: Transforms a review element into a dictionary with relevant information.
"""

from datetime import datetime 
import logging
from src.utils.config import load_config


config = load_config()
logging.basicConfig(filename=config['paths']['log_file'], 
                    level=config['logging']['level'], 
                    format=config['logging']['format'])

def transform_review(review):
    """
    Transforms a review element into a dictionary with relevant information.

    Parameters
    ----------
    review: BeautifulSoup object
        The BeautifulSoup object containing the review HTML element.
    
    Returns
    -------
    dict
        A dictionary containing the transformed review data. Returns an empty dictionary if an error occurs.
    """
    try:
        aside = review.find('aside')
        info_by = aside.get('aria-label')

        span_reviewer = review.find('span', class_='typography_heading-xxs__QKBS8 typography_appearance-default__AAY17')
        reviewer = span_reviewer.text.strip() if span_reviewer else None

        spans = aside.find_all('span')
        location = spans[-1].get_text()

        tor_div = review.find('div', class_='styles_reviewLabels__nHPUT styles_reviewLabels__Ym2vM')
        type_of_review = tor_div.find_all('span')[-1].text.strip() if tor_div else None # type: ignore 

        title = review.find('h2', class_='typography_heading-s__f7029').text.strip()
        paragraph = review.find('p', class_='typography_body-l__KUYFJ')
        paragraph_text = paragraph.text.strip() if paragraph else None
        date_of_experience = review.find('p', class_='typography_body-m__xgxZ_').text.strip().split(': ')[1]
        datetime_posted = review.find('time').get('datetime')

        rated_img = review.find('div', class_='star-rating_starRating__4rrcf star-rating_medium__iN6Ty').find('img') # type: ignore
        rated_alt = rated_img.get('alt') if rated_img else None # type: ignore 
        rated = float(rated_alt.split()[1]) # type: ignore

        reply = review.find('div', class_='styles_wrapper__ib2L5')
        if reply:
            reply_author = reply.find('p', {'data-service-review-business-reply-title-typography': 'true'}).text.strip()
            # reply_date = reply.find('time').text.strip()
            reply_datetime_posted = reply.find('time').get('datetime')
            reply_paragraph = reply.find('p', {'data-service-review-business-reply-text-typography': 'true'}).text.strip()
        else:
            reply_author = None
            # reply_date = None
            reply_datetime_posted = None
            reply_paragraph = None


        return {
            "date" : datetime.now().strftime("%Y-%m-%d %H:%M:%S"), #.strftime('%Y-%m-%d'),
            'info by': info_by,
            'author_name': reviewer,
            'author_location': location,
            'type of review': type_of_review,
            'title': title,
            'rated': rated,
            'time_posted': datetime_posted,
            'paragraph': paragraph_text,
            'date_of_experience': date_of_experience,
            'reply_author': reply_author,
            'reply_date': reply_datetime_posted,
            'reply_paragraph': reply_paragraph
        }
    except Exception as e:
        logging.error(f"Error transforming review ({reviewer}): {e}")
        return {}
