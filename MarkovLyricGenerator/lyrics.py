import configparser
import time

import requests
from bs4 import BeautifulSoup

# Use config.ini to hide security information
def getAccessToken():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['Client_Access_Token']['token']

token = getAccessToken()
headers = {"authorization": token}

def searchMusicArtist(name):
    # {} and .format basically used to insert parameter
    api_url = "https://api.genius.com/search?q={}".format(name)
    # api request takes in header
    r = requests.get(api_url, headers=headers)
    return r.json()

def getArtistID(name):
    r = searchMusicArtist(name)
    # To explore json response, use [] to delve into each array
    id = r["response"]["hits"][0]["result"]["primary_artist"]["id"]
    return id

def getTopTenSongs(name):
    id = getArtistID(name)
    api_url = "https://api.genius.com/artists/{}/songs".format(id)
    params = {
        "sort": "popularity",
        "per_page": 10
    }
    r = requests.get(api_url, headers=headers, params=params)
    return r.json()

def getLyricsArray(name):
    r = getTopTenSongs(name)
    songs = r["response"]["songs"]
    lyrics_array = []
    for song in songs:
        lyrics_array.append(song["url"])
    return lyrics_array

def scrapeLyricText(name):
    links = getLyricsArray(name)
    song_lyrics = []
    for link in links:
        # Get the page using the link
        page = requests.get(link)
        # Parse the html content
        soup = BeautifulSoup(page.content, 'lxml')

        # Find the specific class called 'lyrics'
        lyrics_div = soup.find(class_="lyrics")
        # If condition required; scraping Genius sites are not consistent, anti-measure exists
        if lyrics_div is not None:
            # Get all the anchor tag content
            anchor_tags = lyrics_div.find_all('a')
            current_lyrics = []
            for anchor in anchor_tags:
                if len(anchor.text) > 0 and anchor.text[0] != "[":
                    text = anchor.text.replace("\n", " ")
                    current_lyrics.append(text)
            song_lyrics.append(current_lyrics)
    return song_lyrics
