__author__ = 'Bharadwaj'

from bs4 import BeautifulSoup
import urllib.request
import socket


class Url_Construct:
    def __init__(self, url):
        self.connection_timeout = 10
        self.stock_symbols_summary_urls = {}
        self.home_url = url
        self.html_content = ''
        self.nasdaq_url = ''
        self.nasdaq_url_content = ''
        self.stock_symbols = []

    def execute(self):
        self.set_connection_timeout()
        self.main_url_content()
        self.nasdaq_url_construct()
        self.nasdaq_url_contents()
        self.retrieve_stock_symbols()
        self.stock_symbols_urls_dict()
        return self.stock_symbols_summary_urls

    def set_connection_timeout(self):
        socket.setdefaulttimeout(self.connection_timeout)

    def main_url_content(self):
        self.html_content = BeautifulSoup(urllib.request.urlopen(self.home_url).read().decode('utf8'))

    def nasdaq_url_construct(self):
        self.nasdaq_url = self.home_url + self.html_content.find("a", {"title": "NASDAQ Composite"})['href'].replace('/', '')
        self.html_content = ''

    def nasdaq_url_contents(self):
        self.nasdaq_url_content = BeautifulSoup(urllib.request.urlopen(self.nasdaq_url).read().decode('utf8'))

    def retrieve_stock_symbols(self):
        self.stock_symbols = self.nasdaq_url_content.find("div", {"id": "yfi_index_components"}).\
            find_all("td", {"class": "name"})

    def stock_symbols_urls_dict(self):
        for anchor_tags in self.stock_symbols:
            self.stock_symbols_summary_urls[anchor_tags.find("a").text] = self.home_url + anchor_tags.find("a")['href']