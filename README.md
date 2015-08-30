<b><u>Description:</u></b> This project is concentrated on retrieving the necessary data(from STOCK symbols) from NASDAQ

<b><u>URL:</u></b> http://finance.yahoo.com/

<b><u>About the Package:</u></b> <br />
1) Only one url is taken which is the main url mentioned above (http://finance.yahoo.com/) <br />
2) Based on the main url it constructs the url of NASDAQ (http://finance.yahoo.com/q?s=^ixic) <br />
3) From the NASDAQ page (http://finance.yahoo.com/q?s=^ixic) it takes the top movers from "Index Components" section. <br />
4) From the Index Components section, it takes all the available stock symbols and construct respective urls for those symbols (for example: ARIA - http://finance.yahoo.com/q?s=ARIA)<br />
5) Once the stock symbol url is retrieved, respective summary content (Prev Close, Open, Bid, Ask, etc.) is retrieved from the page using BeautifulSoup package.<br />
6) Once the summary content is retrieved, it then builds the url for calls and puts (Ex: http://finance.yahoo.com/q/op?s=ARIA+Options)<br />
7) From the calls and puts page - it retrieves all the calls and puts (Contract Name, Last, Bid, Ask, etc.) details on that particular day<br />

--> Yahoo/main.py - Main execution file. It takes only one url which is http://finance.yahoo.com/. <br/>
--> Yahoo/calls_and_puts_url_construct.py - This class helps in constructing calls and puts url. <br/>
--> Yahoo/create_csv.py - This class helps in creating and writing the respective csv files for summary, calls and puts content. <br/>
--> Yahoo/get_calls_and_puts.py - This class helps in retrieving the calls and puts from the url which we get from calls_and_puts_url_construct class. <b/>
