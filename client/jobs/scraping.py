
import requests
from bs4 import BeautifulSoup

proxies = {
    "socks5h": "socks5h://127.0.0.1:9050",
    "http": "http://127.0.0.1:8118",
}

# Stronghold Paste
URL = 'http://strongerw2ise74v3duebgsvug4mehyhlpa7f6kfwnas7zofs3kov7yd.onion/all'


def get_landing_page(url: str, proxies):
    """
    Get the HTML page from the URL
    url: URL of the page
    proxies: proxy to use
    return: HTML page
    """
    try:
        response = requests.get(url=url, proxies=proxies)  # get the page
        parser_HTML = BeautifulSoup(
            response.text, 'html.parser')  # parse the page
        return parser_HTML
    except:
        print("Error")


get_lending_page(url=URL, proxies=proxies)
