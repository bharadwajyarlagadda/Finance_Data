Description: This project is concentrated on retrieving the necessary data(from STOCK symbols) from NASDAQ

URL: http://finance.yahoo.com/

1) Only one url is taken which is the main url mentioned above (http://finance.yahoo.com/) <br />
2) Based on the main url it constructs the url of NASDAQ (http://finance.yahoo.com/q?s=^ixic)

3) From the NASDAQ page (http://finance.yahoo.com/q?s=^ixic) it takes the top movers from "Index Components" section.

4) From the Index Components section, it takes all the available stock symbols and construct respective urls for those symbols (for example: ARIA - http://finance.yahoo.com/q?s=ARIA)

5) Once the stock symbol url is retrieved, respective summary content (Prev Close, Open, Bid, Ask, etc.) is retrieved from the page using BeautifulSoup package.

6) Once the summary content is retrieved, it then builds the url for calls and puts (Ex: http://finance.yahoo.com/q/op?s=ARIA+Options)

7) From the calls and puts page - it retrieves all the calls and puts (Contract Name, Last, Bid, Ask, etc.) details on that particular day


