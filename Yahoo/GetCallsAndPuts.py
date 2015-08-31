__author__ = 'Bharadwaj'

# This class helps in retrieving the calls table and puts table
# headers and all the row data.
# Input - 1) Stock symbol
#         2) The url which consists of calls and puts data
# Output - 1) stock symbol
#          2) calls and puts headers
#          3) calls and puts row data

from bs4 import BeautifulSoup
import urllib.request
import socket


class GetCallsAndPuts:
    def __init__(self, stock_symbol, calls_options_url):
        self.connection_timeout = 10
        self.html_content = ''
        self.stock_symbol = stock_symbol
        self.calls_options_url = calls_options_url
        self.calls_div_tag = ''
        self.headers = []
        self.row_data = []
        self.all_rows_data = []
        self.calls_headers = []
        self.calls_rows_data = []
        self.puts_headers = []
        self.puts_rows_data = []

    def execute(self):
        self.set_connection_timeout()
        self.get_options_content()
        self.get_calls_and_puts_content("calls")
        self.get_column_names()
        self.calls_headers, self.calls_rows_data = self.get_rows_data()
        self.clear_values()
        self.get_calls_and_puts_content("puts")
        self.get_column_names()
        self.puts_headers, self.puts_rows_data = self.get_rows_data()
        self.clear_values()
        return self.stock_symbol, self.calls_headers, self.calls_rows_data, self.puts_headers, self.puts_rows_data

    # get_options_content() retrieves the html content from
    # the url which consists of calls and puts data
    def get_options_content(self):
        self.html_content = BeautifulSoup(urllib.request.urlopen(self.calls_options_url).read().decode('utf8'))

    # set_connection_timeout() helps in maintaining the time
    # for the socket. This function is mainly used for
    # retrieving the html_content (eradicating the html errors)
    def set_connection_timeout(self):
        socket.setdefaulttimeout(self.connection_timeout)

    # get_calls_and_puts_content() helps in retrieving the
    # html sections for calls and puts.
    def get_calls_and_puts_content(self, string_calls_or_puts):
        if string_calls_or_puts == "calls":
            self.calls_div_tag = self.html_content.find("div", {"id": "optionsCallsTable"})
            #print(self.calls_div_tag)
        else:
            self.calls_div_tag = self.html_content.find("div", {"id": "optionsPutsTable"})

    # get_column_names() helps in retrieving the calls and
    # puts table headers from the html section which we
    # get from get_calls_and_puts_content().
    def get_column_names(self):
        headers = self.calls_div_tag.find_all("th")
        for header in headers:
            if header.get("data-sort-column"):
                self.headers.append(header.get("data-sort-column"))
            elif header.text == "Contract Name":
                self.headers.append(header.text)
            else:
                continue
        #print(self.headers)

    # get_rows_data() helps in retrieving the calls and puts
    # table content from the html section which we
    # get from get_calls_and_puts_content().
    def get_rows_data(self):
        tbody_tag = self.calls_div_tag.find("tbody")
        rows = tbody_tag.find_all("tr")
        for row in rows:
            td_tags = row.find_all("td")
            for td_tag in td_tags:
                self.row_data.append(td_tag.text.strip('\n'))
            self.all_rows_data.append(self.row_data)
            self.row_data = []
        return self.headers, self.all_rows_data

    # clear_values() - used for memory management
    def clear_values(self):
        self.calls_div_tag = ''
        self.headers = []
        self.row_data = []
        self.all_rows_data = []