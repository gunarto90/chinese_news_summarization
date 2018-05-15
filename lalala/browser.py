#!/usr/bin/python
import urllib2
from bs4 import BeautifulSoup
import re

class ChinatimesNews:
    def __init__(self, url):
        self.url = url
        self.title = None
        self.content = None
        self.root_category = None
        self.category = None
        self.published_date = None

    def __repr__(self):
        return 'url: {}'.format(self.url)

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(self, other.__class__):
            if type(other) is type(self):
                if other.url == self.url:
                    return True
                else:
                    return self.__dict__ == other.__dict__
            else:
                return NotImplemented
        return NotImplemented

    def __ne__(self, other):
        """Overrides the default implementation (unnecessary in Python 3)"""
        x = self.__eq__(other)
        if x is not NotImplemented:
            return not x
        return NotImplemented

    def __hash__(self):
        """Overrides the default implementation"""
        return hash(tuple(sorted(self.__dict__.items())))

def open_link(url):
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    page = response.read()
    return page

def parsing_links(page):
    results = []
    soup = BeautifulSoup(page, 'html.parser')
    anchors = soup.findAll('a')
    for a in anchors:
        if a not in results:
            results.append(a)

    return results

def parsing_html(page):
    soup = BeautifulSoup(page, 'html.parser')
    # print(soup.prettify())

    data = {}
    results = []
    sections = soup.findAll('section', attrs={'class': 'news-list'})
    for section in sections:
        headings = section.findAll('h3')
    
    # headings = soup.findAll('h3')
        for h in headings:
            anchors = h.findAll('a')
            for a in anchors:
                x = ChinatimesNews(a['href'])
                x.content = a.string
                if x not in results:
                    results.append(x)

    return results