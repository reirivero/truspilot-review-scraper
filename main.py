import os
from src.extraction.extract import get_total_pages, extract_reviews 
from src.transformation.transform import transform_review
from src.loading.load import load_data 
from src.utils.config import load_config

def main():
    config = load_config()
    for site, details in config['truspilot'].items():
        url = details['url']
        output_file = os.path.abspath(config['paths'][site]['output_path'])

        total_pages = get_total_pages(url) # type: ignore
        all_reviews = []

        for page in range(1, total_pages + 1):
            page_url = f'{url}?page={page}'
            print(page_url)
            reviews = extract_reviews(page_url) # type: ignore
            for review in reviews:
                all_data_review = transform_review(review)
                # print(all_data_review)
                all_reviews.append(all_data_review)
            # print(all_reviews)
        load_data(all_reviews, output_file)

    
if __name__ == '__main__':
    main()