import pprint
import sys
import os

import spotipy
import spotipy.util as util
import json


#https://open.spotify.com/user/1118158951/playlist/4uAEvLEhJLmzPmmCkIVBHF

if len(sys.argv) > 0:
    playlist_id = '4uAEvLEhJLmzPmmCkIVBHF'
else:
    print("Usage: %s username playlist_id track_id ..." % (sys.argv[0],))
    sys.exit()

clientID = os.getenv('SPOTIPY_CLIENT_ID')
clientSecret = os.getenv('SPOTIPY_CLIENT_SECRET')
redirect = os.getenv('SPOTIPY_REDIRECT_URI')
username = '1118158951'
spotifyusername = 'spotifydiscover'
playlist_id = '4uAEvLEhJLmzPmmCkIVBHF'

new_song_id = "7jqPrUh6IR8nh7qM2gJyyl"

scope = 'playlist-modify-public'
token = util.prompt_for_user_token(username, scope, client_id = clientID, client_secret = clientSecret, redirect_uri = redirect)

# #doshit
# #username - 1118158951
targetCurrSongs = []
sourceSongs = []

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    
    #mainPlaylist = sp.user_playlist(username, playlist_id, fields='tracks, next')
    #items = mainPlaylist['tracks']['items']

    search = sp.search("eminem mosh", limit=10, type="track")
    result = search["tracks"]["items"][0]["external_urls"]["spotify"]
    result2 = search["tracks"]["items"][1]["external_urls"]["spotify"]
    
    print (result +" "+  result2)
    
    playlistSongs = []
    playlists = sp.user_playlist(username, playlist_id, fields="tracks, next")
    for song in playlists["tracks"]["items"]:
        playlistSongs.append(song["track"]["id"])
    
    print(playlistSongs)
    
    if (new_song_id not in playlistSongs):
        sp.user_playlist_add_tracks(username, playlist_id, [new_song_id])

else:
    print("Can't get token for", username)



#spotify:track:1MsyEbEQca1sfC9JnkKnOm
#spotify:track:2ktzBAD5iGVfK1SSE2gFMk


