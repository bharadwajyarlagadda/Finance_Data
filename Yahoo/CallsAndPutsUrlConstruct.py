__author__ = 'Bharadwaj'

# This class helps in constructing the calls and puts
# html url.
# Input - 1) stock symbol
#         2) stock_url (the respective url for the stock symbol)
#         3) url (the main url which is hard coded in Main class)
# Output - 1) stock symbol
#          2) respective stock's calls and puts section url

import socket
from bs4 import BeautifulSoup
import urllib.request


class CallsAndPutsUrlConstruct:
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

    # set_connection_timeout() helps in maintaining the time
    # for the socket. This function is mainly used for
    # retrieving the html_content (eradicating the html errors)
    def set_connection_timeout(self):
        socket.setdefaulttimeout(self.connection_timeout)

    # get_html_content() retrieves the html content from
    # the url which consists of stock data
    def html_content(self):
        self.html_contents = BeautifulSoup(urllib.request.urlopen(self.stock_url).read().decode('utf8'))

    # get_options() helps in retrieving the url which
    # contains the calls and puts data
    def get_options(self):
        options_url = self.html_contents.find_all('a', text='Options')
        for options in options_url:
            if "+Options" in options['href'] and "/q/op" in options['href']:
                self.options_url = self.home_url + options['href'].replace('/', '', 1)
            else:
                pass

    # clear_values() - used for memory management
    def clear_values(self):
        self.html_contents = ''