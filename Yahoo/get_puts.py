__author__ = 'Bharadwaj'

from bs4 import BeautifulSoup
import urllib.request

class get_puts:

    def __init__(self, stock_symbol, calls_options_url):
        self.html_content = ''
        self.stock_symbol = stock_symbol
        self.calls_options_url = calls_options_url
        self.calls_div_tag = ''
        self.headers = []
        self.row_data = []
        self.all_rows_data = []

    def execute(self):
        self.get_options_content()
        self.get_puts_content()
        self.get_column_names()
        self.get_rows_data()

    def get_options_content(self):
        self.html_content = BeautifulSoup(urllib.request.urlopen(self.calls_options_url).read().decode('utf8'))

    def get_puts_content(self):
        self.calls_div_tag = self.html_content.find("div", {"id": "optionsPutsTable"})
        #print(self.calls_div_tag)

    def get_column_names(self):
        headers = self.calls_div_tag.find_all("th")
        for header in headers:
            if header.get("data-sort-column"):
                self.headers.append(header.get("data-sort-column"))
            elif header.text == "Contract Name":
                self.headers.append(header.text)
            else:
                continue
        print(self.headers)

    def get_rows_data(self):
        tbody_tag = self.calls_div_tag.find("tbody")
        rows = tbody_tag.find_all("tr")
        for row in rows:
            td_tags = row.find_all("td")
            for td_tag in td_tags:
                self.row_data.append(td_tag.text.strip('\n'))
            self.all_rows_data.append(self.row_data)
            self.row_data = []
        print(self.all_rows_data)