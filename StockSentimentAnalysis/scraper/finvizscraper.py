from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


def requestSource(tickers):
    # Url to be used to call the web page
    finviz_url = 'https://finviz.com/quote.ashx?t='

    news_tables = {}
    for ticker in tickers:
        url = finviz_url + ticker

        # Calls url given the appropriate agent to access
        req = Request(url=url, headers={'user-agent': 'stockapp'})
        response = urlopen(req)

        # Parse HTML object retrieved by the request lib
        html = BeautifulSoup(response, 'html')
        # Parses HTML object for elements with 'news-table' id
        news_table = html.find(id='news-table')
        news_tables[ticker] = news_table

    return news_tables


def scrape(news_tables):

    parsed_data = []

    # Main scraping method to grab text and date of articles
    # Iterating over items of news_tables objects
    for ticker, news_table in news_tables.items():

        for row in news_table.findAll('tr'):
            # .text is same as get_text()
            title = row.a.get_text()
            # Splits text based on space
            date_data = row.td.text.split(' ')

            # Sometimes date has both date and timestamp, or only timestamp. Account for that edge case
            if len(date_data) == 1:
                time = date_data[0]
            else:
                date = date_data[0]
                time = date_data[1]

            parsed_data.append([ticker, date, time, title])

    return parsed_data

# Old Code:
#
# amd_data = news_tables['AMD']
# // Gives list of all different TR elements in the html passed
# amd_rows = amd_data.findAll('tr')
#
# for index, row in enumerate(amd_rows):
#     // Grabs one of the row's 'a' html tag's text object (<a >text </a>)
#     title = row.a.text
#     timestamp = row.td.text
#     print(timestamp + " " + title)