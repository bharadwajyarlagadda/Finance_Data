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
        self.options_tag_present_bool()

    def set_connection_timeout(self):
        socket.setdefaulttimeout(self.connection_timeout)

    def html_content(self):
        self.html_contents = BeautifulSoup(urllib.request.urlopen(self.stock_url).read().decode('utf8'))

    def options_tag_present_bool(self):
        bool_value = self.get_options()
        print(bool_value)
        if bool_value is True:
            pass
        else:
            print(self.stock_symbol + ": This Stock symbol doesn't have any calls or puts today")

    def get_options(self):
        options_tag_present = False
        options_url = self.html_contents.find_all('a', text='Options')
        for options in options_url:
            if "+Options" in options['href'] and "/q/op" in options['href']:
                print(options)
                self.options_url = self.home_url + options['href'].replace('/', '', 1)
                print(self.options_url)
                self.get_options_content()
                self.get_calls_content()
                options_tag_present = True
            else:
                options_tag_present = False
        return options_tag_present

    def get_options_content(self):
        self.html_contents = BeautifulSoup(urllib.request.urlopen(self.options_url).read().decode('utf8'))

    def get_calls_content(self):
        calls_div_tag = self.html_contents.find("div", {"id": "optionsCallsTable"})
        print(calls_div_tag)