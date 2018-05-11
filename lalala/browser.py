#!/usr/bin/env python
import urllib.request
from bs4 import BeautifulSoup
import re

def open_link(url):
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        page = response.read()
        # page = page.decode('unicode-escape')
        page = str(page).encode('utf-8')
        # print(page)
        return page

def parsing_html(page):
    soup = BeautifulSoup(page, 'html.parser')
    # print(soup.prettify())

    for area in area_list:
        tables = soup.findAll('table', attrs={'class': area})
        for table in tables:
            rows = table.findAll('tr')
            for tr in rows:
                cols = tr.findAll('td')
                for td in cols:
                    text = td.find(text=True)
                    if text is not None:
                        # text = text.replace('\xc2\xb0', 'u"\N{DEGREE SIGN}"')
                        # text = ''.join([i if ord(i) < 128 else ' ' for i in text])
                        # re.sub(r'[^\x00-\x7F]+',' ', text)
                        print(text)
