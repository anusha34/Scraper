from bs4 import BeautifulSoup
import json

# todo: is there a reason you used urllib.request insteas of the default request library?
# try and use that if possible. either way, remove the import that isn't used when you are done
from urllib.request import urlopen
import requests

### General todos:
# Do each of these, commit after each change clearly stating which one you fixed
# todo: 1. Remove commented out lines of code (not regular comments)
# todo: 2. Add comments to explain a little more
# todo: 3. use refactor>rename in pycharm to rename your variables to *not use* abbreviations
# (i.e. con_list should be content_list, pg -> page, ima_x -> immaculatta_x)
# todo: 4. use refactor>rename in pycharm to rename your variables to *use* extra descriptions
# (i.e. html_page should be immaculatta_html, soup -> immaculatta_soup, key -> university etc.)
# todo: 5. follow the other todo instructions throughout this file
# todo: 6. Delete all these todo comments (including thsi list) when you are done

# region region-content class for immaculata
def parse_immaculata(page):
    soup = BeautifulSoup(page, 'html.parser')
    c_list = soup.find(class_='region region-content')
    c_list_items = c_list.find_all('a')
    for c_name in c_list_items:
        content = c_name.get_text()
        link = c_name.get('href')
        ima_dict = {
            # "context": text,
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
        #title_ix(dict_list1)
    # print(dictList1)
    # s = open(key + '.txt', 'a+')
    # s.write(str(names) + "\n")
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
            # "text": text,
            "url": link,
            "content": content
        }
        html_page = urlopen(link)
        soup = BeautifulSoup(html_page, 'html.parser')
        con_list = soup.find(id='main')
        con_items = con_list.find_all(['p', 'ul'])
        for con_name in con_items:
            text_list = con_name.get_text().encode('UTF8')
        urs_dict["text"] = str(text_list)
        dict_list2.append(urs_dict)
        #title_ix(dict_list2)
    # print(dictList2)
    # print(dictList2)
    # s = open(key + '.txt', 'a+')
    # s.write(str(names) + "\n")
    print('Parsed Ursinus')
    return dict_list2

# todo: mose these into the functions they belong in, they aren't needed here,
# also, they both can be called just <universityname>_link_list or something
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

for key in universities:
    url = university_urls[key]
    # print(url)
    pg = urlopen(url)
    #todo: read_func should be called something else more descriptive - maybe university_link_list?
    read_func = university_funcs[key](pg)
    title_ix_data[key] = read_func

#todo: you can add code to write this to a file called 'pa_title_ix.json' instead.
print(title_ix_data)


#for university in universities:
#    title_ix_data[university] = university_funcs[university]()
#print(title_ix_data)


