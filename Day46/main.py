import requests
from bs4 import BeautifulSoup


# date = input("Which year you want to travel.Enter the year in YYYY-MM-DD format.")
date = "2010-08-12"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
url = "https://www.billboard.com/charts/hot-100/" + date
response = requests.get(url=url, headers=header)
billboard_webpage = response.text

song_soup = BeautifulSoup(billboard_webpage, "html.parser")
song_names = []
artists = []
artist_soup = song_soup.select('div>ul>li>ul>li>span.a-no-trucate.a-font-primary-s')
# for artist in artist_soup:
#     artists.append(artist.getText().split())

for song in song_soup.select('div>ul>li>ul>li>h3'):
    song_names.append(song.getText().split())

