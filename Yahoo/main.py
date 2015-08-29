__author__ = 'Bharadwaj'

from Yahoo import url_construct
from Yahoo import stock_symbol_summary
from Yahoo import create_csv
from Yahoo import calls_and_puts_url_construct

url = "http://finance.yahoo.com/"

yahoo_Url_Construct = url_construct.yahoo_Url_Construct(url)
stock_symbols_summary_urls = yahoo_Url_Construct.execute()
print(stock_symbols_summary_urls)
for key, values in stock_symbols_summary_urls.items():
    calls_and_puts_url = calls_and_puts_url_construct.calls_and_puts_url_construct\
        (key, stock_symbols_summary_urls[key], url)
    calls_and_puts_url.execute()
    break

#for key, values in stock_symbols_summary_urls.items():
#    stock_symbol_summ = stock_symbol_summary.stock_symbol_summary(key, stock_symbols_summary_urls[key])
#    stock_symbol, values = stock_symbol_summ.execute()
#    create_csv_writer = create_csv.create_csv(stock_symbol, values)
#    create_csv_writer.execute()