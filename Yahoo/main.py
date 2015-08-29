__author__ = 'Bharadwaj'

import url_construct
import stock_symbol_summary
import create_csv

yahoo_Url_Construct = url_construct.yahoo_Url_Construct()
stock_symbols_summary_urls = yahoo_Url_Construct.execute()
#print(stock_symbols_summary_urls)
for key, values in stock_symbols_summary_urls.items():
    stock_symbol_summ = stock_symbol_summary.stock_symbol_summary(key, stock_symbols_summary_urls[key])
    stock_symbol, values = stock_symbol_summ.execute()
    create_csv_writer = create_csv.create_csv(stock_symbol, values)
    create_csv_writer.execute()