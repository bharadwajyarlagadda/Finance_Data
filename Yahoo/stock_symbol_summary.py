__author__ = 'Bharadwaj'

# This class helps in retrieving the stock's summary data.
# Input - 1) stock symbol
#         2) stock symbol's url
# Output - 1) stock symbol
#          2) stock symbol's summary data

from bs4 import BeautifulSoup
import urllib.request
import socket


class stock_symbol_summary:
    def __init__(self, stock_symbol, stock_symbol_summary_url):
        self.connection_timeout = 10
        self.stock_symbol = stock_symbol
        self.stock_summary_url = stock_symbol_summary_url
        self.values = {}
        self.html_content = ''

    def execute(self):
        self.set_connection_timeout()
        self.retrieve_html_summary_stock_symbol()
        self.retrieve_div_tag()
        self.clear_values()
        return self.stock_symbol, self.values

    # set_connection_timeout() helps in maintaining the time
    # for the socket. This function is mainly used for
    # retrieving the html_content (eradicating the html errors)
    def set_connection_timeout(self):
        socket.setdefaulttimeout(self.connection_timeout)

    # retrieve_html_summary_stock_symbol() helps in retrieving
    # the html content for the respective stock symbol
    def retrieve_html_summary_stock_symbol(self):
        #print(self.stock_summary_url)
        self.html_content = BeautifulSoup(urllib.request.urlopen(self.stock_summary_url).read().decode('utf8'))

    # retrieve_div_tag() helps in retrieving the summary content
    # out of the stock symbol's url
    def retrieve_div_tag(self):
        values = self.html_content.find("div", {"id": "yfi_quote_summary_data"}).find_all("tr")
        for value in values:
            values_key = value.find("th").text
            values_val = value.find("td").text
            self.values[values_key] = values_val
        #print(self.values)

    def clear_values(self):
        self.html_content = ''