
from black import main
import requests
from bs4 import BeautifulSoup

proxies = {
    "socks5h": "socks5h://127.0.0.1:9050",
    "http": "http://127.0.0.1:8118",
}

config_website = {
    "title": "h4",
    "author": ".col-sm-6"

}
# Stronghold Paste
URL = 'http://strongerw2ise74v3duebgsvug4mehyhlpa7f6kfwnas7zofs3kov7yd.onion/all?page='


# ---------- GET LANDING PAGE FOR WEBSITE WITH URL ---------- #
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

# ---------- GET PASTES FROM WEBSITE ---------- #


def get_pastes_list(parser_HTML):
    """
    Get the list of pastes from the HTML page
    parser_HTML: HTML page
    return: list of pastes
    """
    pastes_list = []
    for paste in parser_HTML.find_all('div', class_='row'):
        pastes_list.append(paste)
    return pastes_list

# ---------- GET PASTE INFO ---------- #


def get_paste_info(paste):
    """
    Get the information of the paste
    paste: paste
    return: dictionary with the information
    """
    try:
        paste_info = {}
        paste_info['title'] = paste.find(config_website["title"]).text.strip()
        paste_info['author'] = paste.find(
            "div", class_="col-sm-6").text.strip().split(" ")[2]
        paste_info['date'] = " ".join(paste.find(
            "div", class_="col-sm-6").text.strip().split(" ")[4:])
        paste_info["content"] = find_paste_content(
            url=find_paste_link(paste), proxies=proxies)
        return paste_info
    except:
        return

# ---------- GET PASTE LINK ---------- #


def find_paste_link(paste):
    """
    Get the link of the paste
    paste: paste
    return: link of the paste
    """
    return paste.find("a")['href']

# ---------- GET PASTE CONTENT ---------- #


def find_paste_content(url, proxies):
    content = ""
    html = get_landing_page(url=url, proxies=proxies)
    li_content = html.find("ol").find_all("li")
    for li in li_content:
        content += li.text + "\n"
    return content

# ---------- GET AMOUNT OF PAGES ---------- #


def get_amount_of_pages(parser_HTML):
    """
    Get the amount of pages
    parser_HTML: HTML page
    return: amount of pages
    """
    return len(parser_HTML.find("ul", class_="pagination").find_all("li")) - 2  # -2 because the first and last are not pages


# ---------- SCRAPING ---------- #
def scraper():
    """
    scraper function
    """
    for page in range(1, get_amount_of_pages(get_landing_page(URL, proxies)) + 1):
        for paste in get_pastes_list(get_landing_page(URL+str(page), proxies)):
            paste_info = get_paste_info(paste)
            if paste_info:
                print(paste_info)
                print("\n")
