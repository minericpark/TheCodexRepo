from scraper import finvizscraper
from sentimentplotter import stocksentimentplotter
from sentimentanalyzer import sentimentanalyzer

tickers = ['AMD', 'AQN', 'AAPL']

news_tables = finvizscraper.requestSource(tickers)

parsed_data = finvizscraper.scrape(news_tables)

df = sentimentanalyzer.analyze(parsed_data)

stocksentimentplotter.plot(df)

# Implement Jupyter instead of Pandas next time
# Consider creating a better sentiment analyzer for stock articles specifically
