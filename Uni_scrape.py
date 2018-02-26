
from bs4 import BeautifulSoup
import json
from urllib.request import urlopen
import requests


#region region-content class for immaculata
def parse_immaculata(page):
    soup = BeautifulSoup(page, 'html.parser')
    c_list = soup.find(class_='region region-content')
    c_list_items = c_list.find_all('a')
    for c_name in c_list_items:
        content = c_name.get_text()
        link = c_name.get('href')
        ima_dict = {
            #"context": text,
            "url": link,
            "content": content
        }
        html_page = urlopen(link)
        soup = BeautifulSoup(html_page, 'html.parser')
        con_list = soup.find(class_='region region-content')
        con_items = con_list.find_all('div')
        for con_name in con_items:
            text_list = con_name.get_text().encode('UTF8')
        ima_dict["text"] = str(text_list)
        dict_list1.append(ima_dict)
        title_ix(dict_list1)
    #print(dictList1)
            #s = open(key + '.txt', 'a+')
            #s.write(str(names) + "\n")
    print('Parsed Immaculata')
    return dict_list1


# class for ursinus : lw_subnav (for links) and editable (for content)
def parse_ursinus(page):
    soup = BeautifulSoup(page, 'html.parser')
    c_list = soup.find(class_='lw_subnav')
    c_list_items = c_list.find_all('a')
    for c_name in c_list_items:
        content = c_name.get_text()
        url = c_name.get('href')
        link = 'http://www.ursinus.edu' + url
        urs_dict = {
            #"text": text,
            "url": link,
            "content": content
            }
        html_page = urlopen(link)
        soup = BeautifulSoup(html_page, 'html.parser')
        con_list = soup.find(id='main')
        con_items = con_list.find_all([ 'p', 'ul' ])
        for con_name in con_items:
            text_list = con_name.get_text().encode('UTF8')
        urs_dict["text"] = str(text_list)
        dict_list2.append(urs_dict)
        title_ix(dict_list2)
    #print(dictList2)
        #print(dictList2)
            #s = open(key + '.txt', 'a+')
            #s.write(str(names) + "\n")
    print('Parsed Ursinus')
    return dict_list2

def title_ix(dict_list1, dict_list2):
    title_ix_data = {
        "Immaculata": dict_list1,
        "Ursinus": dict_list2
    }
    print("visited")
    print(title_ix_data)


dict_list1 = []
dict_list2 = []
universities = ["Immaculata", "Ursinus"]
university_urls = {
    'Immaculata': 'http://www.immaculata.edu/titleix',
    'Ursinus': 'http://www.ursinus.edu/student-life/handbook/sexual-and-gender-based-misconduct'
    }
university_funcs = {
    'Immaculata': parse_immaculata,
    'Ursinus': parse_ursinus
}

for key in universities:
    url = university_urls[key]
    #print(url)
    pg = urlopen(url)
    university_funcs[key](pg)


