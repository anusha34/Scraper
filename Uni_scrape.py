from bs4 import BeautifulSoup
import json
from urllib.request import urlopen
import requests


# region region-content class for immaculata
def parse_immaculata(page):
    immaculata_soup = BeautifulSoup(page, 'html.parser')
    content_list = immaculata_soup.find(class_='region region-content')
    content_list_items = content_list.find_all('a')
    for content_name in content_list_items:
        content = content_name.get_text()
        link = content_name.get('href')
        immaculata_dict = {
            "url": link,
            "content": content
        }
        immaculata_html = urlopen(link)
        immaculata_soup = BeautifulSoup(immaculata_html, 'html.parser')
        content_list = immaculata_soup.find(class_='region region-content')
        content_items = content_list.find_all('div')
        for content_name in content_items:
            text_list = content_name.get_text().encode('UTF8')
        immaculata_dict["text"] = str(text_list)
        dict_list1.append(immaculata_dict)
    print('parsed Immacula')
    return dict_list1


# class for ursinus : lw_subnav (for links) and editable (for content)
def parse_ursinus(page):
    ursinus_soup = BeautifulSoup(page, 'html.parser')
    content_list = ursinus_soup.find(class_='lw_subnav')
    content_list_items = content_list.find_all('a')
    for content_name in content_list_items:
        content = content_name.get_text()
        url = content_name.get('href')
        link = 'http://www.ursinus.edu' + url
        ursinus_dict = {
            "url": link,
            "content": content
        }
        ursinus_html = urlopen(link)
        ursinus_soup = BeautifulSoup(ursinus_html, 'html.parser')
        content_list = ursinus_soup.find(id='main')
        content_items = content_list.find_all(['p', 'ul'])
        for content_name in content_items:
            text_list = content_name.get_text().encode('UTF8')
        ursinus_dict["text"] = str(text_list)
        dict_list2.append(ursinus_dict)
    print('Parsed Ursinus')
    return dict_list2


dict_list1 = []
dict_list2 = []

title_ix_data = {}

universities = ["Immaculata", "Ursinus"]

university_funcs = {
    'Immaculata': parse_immaculata,
    'Ursinus': parse_ursinus
}

university_urls = {
    'Immaculata': 'http://www.immaculata.edu/titleix',
    'Ursinus': 'http://www.ursinus.edu/student-life/handbook/sexual-and-gender-based-misconduct'
}

for university in universities:
    url = university_urls[university]
    page = urlopen(url)
    read_func = university_funcs[university](page)
    title_ix_data[university] = read_func

print(title_ix_data)