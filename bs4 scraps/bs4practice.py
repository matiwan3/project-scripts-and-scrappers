import requests
from bs4 import BeautifulSoup
import re # in case regular expression is required

def getSoup(url: str):
    """
    >>> Args:
        url (str): provide a URL to request

    >>> Returns:
        soup (class): returns a bs4 soup class according to provided URL response 
    """
    search_url = url
    response = requests.get(search_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(type(soup))
    return soup
        
def olx_categories():
    """prints a list of OLX main page categories"""
    url_olx = 'https://www.olx.pl/'
    soup = getSoup(url_olx)
    categories_container = soup.find('div', {'data-testid': 'home-categories-menu-row'}) # find categories container
    categories_found = categories_container.find_all('a')
    
    print(f'[*] Found {len(categories_found)} categories')
    for index, a_tag in enumerate(categories_found, start=1):
        # Find the span within each 'a' tag and print its text
        span = a_tag.find('span')
        if span:
            print(f"[{index}] {span.text}")

def fetch_free_categories():
    olx_for_free_page = 'https://www.olx.pl/oddam-za-darmo/'
    soup = getSoup(olx_for_free_page)

olx_categories()