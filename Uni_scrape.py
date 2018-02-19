
from bs4 import BeautifulSoup
import json
from urllib.request import urlopen
import requests

dictList = []

#universities = ['Immaculata','Ursinus']

university_urls = {
    'Immaculata' : 'http://www.immaculata.edu/titleix',
    'Ursinus' : 'http://www.ursinus.edu/student-life/handbook/sexual-and-gender-based-misconduct'
    }

#region region-content class for immaculata
def parse_immaculata(key):
    urls = university_urls[key]
    page = urlopen(urls)
    soup = BeautifulSoup(page, 'html.parser')
    c_list = soup.find(class_='region region-content')
    c_list_items = c_list.find_all('a')
    for c_name in c_list_items:
        names = c_name.get_text()
        link = c_name.get('href')
        html_page = urlopen(link)
        soup = BeautifulSoup(html_page, 'html.parser')
        con_list = soup.find(class_='region region-content')
        con_items = con_list.find_all('div')
        for con_name in con_items:
            names = con_name.get_text().encode('UTF8')
            s = open(key + '.txt', 'a+')
            s.write(str(names) + "\n")
    print('Parsed Immaculata')

# class for ursinus : lw_subnav (for links) and editable (for content)
def parse_ursinus(key):
    urls = university_urls[key]
    page = urlopen(urls)
    soup = BeautifulSoup(page, 'html.parser')
    c_list = soup.find(class_='lw_subnav')
    c_list_items = c_list.find_all('a')
    for c_name in c_list_items:
        url = c_name.get('href')
        link = 'http://www.ursinus.edu' + url
        html_page = urlopen(link)
        soup = BeautifulSoup(html_page, 'html.parser')
        content_list = soup.find(id='main')
        content_items = content_list.find_all(['p', 'ul'])
        for content_items_list in content_items:
            names = content_items_list.get_text().encode('UTF8')
            s = open(key + '.txt', 'a+')
            s.write(str(names) + "\n")
    print('Parsed Ursinus')

parse_immaculata("Immaculata")
parse_ursinus("Ursinus")