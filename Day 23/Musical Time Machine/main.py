import os

import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

# ----------------------------- Constants ----------------------------- #
song1 = "c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 " \
        "u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 " \
        "u-max-width-230@tablet-only u-letter-spacing-0028@tablet"

song2 = "c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet " \
        "lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 " \
        "u-max-width-230@tablet-only"

# ----------------------------- Starting Program ----------------------------- #

date = input("What year would you like to travel to? Enter in YYYY-MM-DD format:\n")
date = date.split('-')
year = date[0]
month = date[1]
day = date[2]

# --------------------- Web Scraping --------------------- #

billboard_url = f"https://www.billboard.com/charts/hot-100/{year}-{month}-{day}/"
response = requests.get(billboard_url)
web_page = response.text

# List to store all songs
list_of_songs = []

# Using beautifulsoup
soup = BeautifulSoup(web_page, "html.parser")

# First Song
songs = soup.find("h3", class_=song1)
list_of_songs.append(songs.text.strip())

# Rest of the list
# I now have a list of all the songs.
songs = soup.find_all("h3", class_=song2)
for song in songs:
    list_of_songs.append(song.text.strip())

# ------------------------ Authenticating User using Spotipy ------------------------ #
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=os.environ["SPOTIPY_CLIENT_ID"],
        client_secret=os.environ["SPOTIPY_CLIENT_SECRET"],
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

uri_list = []

for song in list_of_songs:
    result = sp.search(q=f'track:{song} year:{year}', type='track')
    try:
        uri = result["tracks"]["items"][0]["uri"]
        uri_list.append(uri)
    except IndexError:
        # print(f"{song} doesn't exist in Spotify. Skipped.")
        pass

# ---------- Creating a new playlist ----------------- #

playlist_id = sp.user_playlist_create(user=user_id, name=f'{year}-{month}-{day} Billboard 100', public=True,
                                      collaborative=False,
                                      description=f'This is the playlist of Billboard Top 100 on {day}/{month}/{year}')

# ----------------- Adding songs to PlayList ----------------- #

sp.playlist_add_items(playlist_id=playlist_id['id'], items=uri_list, position=None)
