
from bs4 import BeautifulSoup
import json
from urllib.request import urlopen
import re
import requests

#from urllib3 import request
#import nltk
#import webbrowser
#import sys

dictList = []

#universities = ['Immaculata','Ursinus']

university_urls = {
    'Immaculata' : 'http://www.immaculata.edu/titleix',
    'Ursinus' : 'http://www.ursinus.edu/student-life/handbook/sexual-and-gender-based-misconduct/'
    }

def parse_ursinus(k = "Ursinus"):
    # class for ursinus : lw_subnav (for links) and editable (for content)
    urls = university_urls[k]
    page = urlopen(urls)
    # print(url)
    soup = BeautifulSoup(page, 'html.parser')
    c_list = soup.find(class_='lw_subnav')
    c_list_items = c_list.find_all('a')
    for c_name in c_list_items:
        names = c_name.get_text()
        link = c_name.get('href')
        html_page = urlopen(link)
        soup = BeautifulSoup(html_page, 'html.parser')
        con_list = soup.find(class_='editable')
        con_items = con_list.find_all('div')
        for con_name in con_items:
            names = con_name.get_text().encode('UTF8')
            s = open(k + '.txt', 'a+')
            s.write(str(names) + "\n")
    print('Parsed Ursinus')

#region region-content class for immaculata
def parse_immaculata(k = "Immaculata"):
    urls = university_urls[k]
    page = urlopen(urls)
    #print(url)
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
            s = open(k + '.txt', 'a+')
            s.write(str(names) + "\n")
    print('Parsed Immaculata')

parse_ursinus()
parse_immaculata()