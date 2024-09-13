from functools import wraps
from time import perf_counter
from typing import Callable, Any
import requests
from bs4 import BeautifulSoup

def handle_http_request(func):
    @wraps(func)
    def wrapper(url, *args, **kwargs):
        response = requests.get(url)
        if response.status_code != 200:
            raise requests.exceptions.HTTPError(f'Error en la solicitud: {response.status_code}')
        soup = BeautifulSoup(response.content, 'html.parser')
        return func(url, soup, *args, **kwargs)
    return wrapper

def get_time(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:

        # Note that timing your code isn't the most reliable option
        # for timing your code. Look into the timeit module for more accurate
        # timing.
        start_time: float = perf_counter()
        result: Any = func(*args, **kwargs)
        end_time: float = perf_counter()

        print(f'"{func.__name__}()" executed in {end_time - start_time:.3f} seconds.')
        return result
    
    return wrapper