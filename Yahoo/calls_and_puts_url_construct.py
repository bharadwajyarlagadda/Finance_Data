__author__ = 'Bharadwaj'

import socket
from bs4 import BeautifulSoup
import urllib.request

class calls_and_puts_url_construct:
    def __init__(self, stock_symbol, stock_url, url):
        self.connection_timeout = 10
        self.stock_symbol = stock_symbol
        self.stock_url = stock_url
        self.home_url = url
        self.html_contents = ''
        self.options_url = ''

    def execute(self):
        print(self.stock_symbol, self.stock_url)
        self.set_connection_timeout()
        self.html_content()
        self.get_options()
        return self.stock_symbol, self.options_url

    def set_connection_timeout(self):
        socket.setdefaulttimeout(self.connection_timeout)

    def html_content(self):
        self.html_contents = BeautifulSoup(urllib.request.urlopen(self.stock_url).read().decode('utf8'))

    def get_options(self):
        options_url = self.html_contents.find_all('a', text='Options')
        for options in options_url:
            if "+Options" in options['href'] and "/q/op" in options['href']:
                self.options_url = self.home_url + options['href'].replace('/', '', 1)
            else:
                pass