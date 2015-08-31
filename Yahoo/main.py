__author__ = 'Bharadwaj'

# This is the main class for execution
# Input: Main url (http://finance.yahoo.com/)
# Output: 1) Yahoo_Data/Yahoo_NASDAQ_Stock_Summary folder - Stock Summary csv files
#         2) Yahoo_Data/Yahoo_NASDAQ_Stock_Calls folder - Stock Calls csv files
#         3) Yahoo_Data/Yahoo_NASDAQ_Stock_Puts folder - Stock Puts csv files

from Yahoo import UrlConstruct
from Yahoo import StockSymbolSummary
from Yahoo import CreateCsv
from Yahoo import CallsAndPutsUrlConstruct
from Yahoo import GetCallsAndPuts


class Main:
    def __init__(self, url):
        self.finance_url = url
        self.stock_symbol = ''
        self.summary_values = {}
        self.stock_symbols_summary_urls = {}
        self.calls_headers = []
        self.calls_rows_data = []
        self.puts_headers = []
        self.puts_rows_data = []

    def execute(self):
        self.stock_sym_summary_urls()
        self.stock_sym_summary()
        self.get_calls_and_puts()

    def stock_sym_summary_urls(self):
        yahoo_url_construct = UrlConstruct.UrlConstruct(self.finance_url)
        self.stock_symbols_summary_urls = yahoo_url_construct.execute()

    def stock_sym_summary(self):
        for key, values in self.stock_symbols_summary_urls.items():
            stock_symbol_summ = StockSymbolSummary.StockSymbolSummary(key, self.stock_symbols_summary_urls[key])
            self.stock_symbol, self.summary_values = stock_symbol_summ.execute()
            self.create_csv_file()
            self.clear_values()

    def create_csv_file(self):
        create_csv_writer = CreateCsv.CreateCsv(self.stock_symbol, self.summary_values, self.calls_headers, self.
                                                  calls_rows_data, self.puts_headers, self.puts_rows_data)
        create_csv_writer.execute()

    def get_calls_and_puts(self):
        for key, values in self.stock_symbols_summary_urls.items():
            calls_and_puts_url = CallsAndPutsUrlConstruct.\
                CallsAndPutsUrlConstruct(key, self.stock_symbols_summary_urls[key], self.finance_url)
            self.stock_symbol, options_url = calls_and_puts_url.execute()
            if options_url:
                print("Retrieved options_url: " + options_url)
                retrieve_get_calls = GetCallsAndPuts.GetCallsAndPuts(self.stock_symbol, options_url)
                self.stock_symbol, self.calls_headers, self.calls_rows_data, self.puts_headers, self.puts_rows_data\
                    = retrieve_get_calls.execute()
                self.create_csv_file()
                self.clear_values()
            else:
                print(self.stock_symbol + ": This Stock symbol doesn't have any calls or puts today")

    def clear_values(self):
        self.stock_symbol = ''
        self.summary_values = {}
        self.calls_headers = []
        self.calls_rows_data = []
        self.puts_headers = []
        self.puts_rows_data = []

if __name__ == '__main__':
    main_object = Main("http://finance.yahoo.com/")
    main_object.execute()