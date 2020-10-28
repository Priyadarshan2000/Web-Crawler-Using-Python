import tkinter as tk
import requests
import main
import html5lib
from bs4 import BeautifulSoup

def scrapped():

    a = get_entry()
    get_request(a)

def get_entry():
    return main.URL_entry.get()

def get_request(a): 
    r = requests.get(a)
    htmlcontent = r.content
    soup = BeautifulSoup(htmlcontent, 'html.parser')

    main.text_widget.insert(tk.END, soup)

def data_entry_in_text_widget():
    pass

    # print(soup)
    # text = r.text 
    # with open("open.txt", "w", encoding='utf-8') as f:
    #     f.write(str(soup))  
    # print(text)
