from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd


def analyze(data):
    # Our data not very efficient, turn it into a data structure that is effective
    df = pd.DataFrame(data, columns=['ticker', 'date', 'time', 'title'])
    # Access datastructure like df['title'] to access title of object

    vader = SentimentIntensityAnalyzer()

    # Creates a mini lambda function that returns a compound score for the given title
    f = lambda title: vader.polarity_scores(title)['compound']
    # Applies the f function on all compound objects within the df
    df['compound'] = df['title'].apply(f)
    # Takes date column and converts it from string to date format
    df['date'] = pd.to_datetime(df.date).dt.date

    return df