import requests
import main
import html5lib
from bs4 import BeautifulSoup

def scrapped():

    a = get_entry()
    print(a)

    r = requests.get(a)
    print(r.text)

def get_entry():
    return main.URL_entry.get()
