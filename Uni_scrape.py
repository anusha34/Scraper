from bs4 import BeautifulSoup
from urllib.request import urlopen


# region region-content class for immaculata
#The function parses the immaculata university webpage to find all the information on title - ix
def parse_immaculata(page):
    # immaculata_list stores the all the immaculata_dict data as a list
    immaculata_list = []
    # fetches all the html content of the page
    immaculata_soup = BeautifulSoup(page, 'html.parser')
    #finds all the parts of the page which have  'region region-content' as it's class
    content_list = immaculata_soup.find(class_='region region-content')
    # finds all 'a' tags within the class
    content_list_items = content_list.find_all('a')
    #loops through individual tags
    for content_name in content_list_items:
        #gets the text describing the tag
        content = content_name.get_text()
        #gets the content in the href tag(url)
        link = content_name.get('href')
        # writes the url and the text to the immaculata_dict
        immaculata_dict = {
            "url": link,
            "content": content
        }
        #opens the urls just fetched
        immaculata_html = urlopen(link)
        # fetches all the html content of the page
        immaculata_soup = BeautifulSoup(immaculata_html, 'html.parser')
        content_list = immaculata_soup.find(class_='region region-content')
        # finds all 'div' tags within the class
        content_items = content_list.find_all('div')
        for content_name in content_items:
            #finds all the text within the class
            text_list = content_name.get_text().encode('UTF8')
        # Writes data as "text" as key to the immaculata_dict dictionary
        immaculata_dict["text"] = str(text_list)
        # All the data immaculata_dict is combined as a list
        immaculata_list.append(immaculata_dict)
    print('parsed Immaculata')
    return immaculata_list


# class for ursinus : lw_subnav (for links) and editable (for content)

#The function parses the Ursinus university webpage to find all the information on title - ix
def parse_ursinus(page):
    # ursinus_list stores the all the ursinus_dict data as a list
    ursinus_list = []
    ursinus_soup = BeautifulSoup(page, 'html.parser')
    # finds all the parts of the page which have  'lw_subnav' as it's class
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
        # finds all the parts of the page which have  'main' as it's id
        content_list = ursinus_soup.find(id='main')
        # Finds all the 'p' and 'ul' tags within the id.
        content_items = content_list.find_all(['p', 'ul'])
        for content_name in content_items:
            text_list = content_name.get_text().encode('UTF8')
        ursinus_dict["text"] = str(text_list)
        ursinus_list.append(ursinus_dict)
    print('Parsed Ursinus')
    return ursinus_list

# Dictionary to store all the data
title_ix_data = {}

#List of universities to be visited by the code
universities = ["Immaculata", "Ursinus"]

#dictionary to call the functions with university name being the key.
university_funcs = {
    'Immaculata': parse_immaculata,
    'Ursinus': parse_ursinus
}

# Main urls of all universities( Entry point for data scraping )
university_urls = {
    'Immaculata': 'http://www.immaculata.edu/titleix',
    'Ursinus': 'http://www.ursinus.edu/student-life/handbook/sexual-and-gender-based-misconduct'
}

for university in universities:
    # Fetches the url with university name as the key
    url = university_urls[university]
    # Opens the url to read the data
    page = urlopen(url)
    # The statements call the function for a particular university
    university_func_call = university_funcs[university](page)
    # A dictionary title_ix_data is created with university being the key and the data is the list created in each functions
    title_ix_data[university] = university_func_call
# Writes data to a json file
write_data = open('pa_title_ix.json', 'a+')
write_data.write(str(title_ix_data) + "\n")
