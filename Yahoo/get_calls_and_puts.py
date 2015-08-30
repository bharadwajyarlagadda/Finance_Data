__author__ = 'Bharadwaj'

from bs4 import BeautifulSoup
import urllib.request

class get_calls_and_puts:

    def __init__(self, stock_symbol, calls_options_url):
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
        self.get_options_content()
        self.get_calls_content("calls")
        self.get_column_names()
        self.calls_headers, self.calls_rows_data = self.get_rows_data()
        self.clear_values()
        self.get_calls_content("puts")
        self.get_column_names()
        self.puts_headers, self.puts_rows_data = self.get_rows_data()
        self.clear_values()
        print(self.calls_headers, self.calls_rows_data)
        print(self.puts_headers, self.puts_rows_data)

    def get_options_content(self):
        self.html_content = BeautifulSoup(urllib.request.urlopen(self.calls_options_url).read().decode('utf8'))

    def get_calls_content(self, string_calls_or_puts):
        if string_calls_or_puts == "calls":
            self.calls_div_tag = self.html_content.find("div", {"id": "optionsCallsTable"})
            #print(self.calls_div_tag)
        else:
            self.calls_div_tag = self.html_content.find("div", {"id": "optionsPutsTable"})

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

    def clear_values(self):
        self.headers = []
        self.row_data = []
        self.all_rows_data = []