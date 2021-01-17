from __future__ import unicode_literals
from youtubesearchpython import VideosSearch
import youtube_dl
import os

# get link
def getlink (search):
    search = search + " audio"
    videosSearch = VideosSearch(search, limit = 1)
    link = 'https://www.youtube.com/watch?v=' + (((videosSearch.result())["result"])[0])["id"]
    return link

# ydl link downloading
def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


def download_link (link):
    os.system("youtube-dl --extract-audio --audio-format wav -o " + mysearch + ".wav " + link)

# example usage case
# change        txt below this txt       to whatever song that you want to download and run the application!
mysearch = "radioactive imagine dragons".replace(" ", "_")
link = getlink(mysearch)
download_link(link)
