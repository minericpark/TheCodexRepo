import configparser
import requests

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
    sortParam = "popularity"
    numPerPage = 10
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

print(getLyricsArray("drake"))