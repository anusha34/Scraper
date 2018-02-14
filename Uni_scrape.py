
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import requests
#from urllib3 import request
import nltk
import webbrowser
import json
import sys

dictList = []

with open("urls.txt") as f:
    urls = f.read()
    a = urls.split('\n')
    x = re.findall(r'http://www.(.*?).edu',urls,re.DOTALL)
    for name in x:
        s = open(name + '.txt','a+')
    for url in a:
        page = urlopen(url)

#page = urlopen('http://www.immaculata.edu/titleix')

soup = BeautifulSoup(page, "html.parser")

def write_json_dict(dict, path):
    file = open(path, 'w+')
    file.write(json.dumps(dict))
    file.close()

c_list = soup.find(class_='region region-content')
c_list_items = c_list.find_all('a')

for c_name in c_list_items:
    names = c_name.get_text()
    links = c_name.get('href')
    dic = names + "," + links
    elements = dic.rstrip().split(",")
    dictList.append(dict(zip(elements[::2], elements[1::2])))
#json_string = json.dumps(dictList)
#print(json_string)
write_json_dict(dictList, 'url.json')
json_data = json.load(open('url.json'))
fetch_url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str(json_data))
a= ','.join(fetch_url)
u=  a.rstrip('').split(",")
for line in u:
    string = line[:-1]
    html_page = urlopen(string)
soup = BeautifulSoup(html_page, "html.parser")

c_list = soup.find(class_='region region-content')
c_items = c_list.find_all('div')
# Use .get_text() to pull out the <div> tag’s children
for c_name in c_items:
    names = c_name.get_text().encode('UTF-8')
    s.write(str(names)+"\n")
 #    s.close()
    
