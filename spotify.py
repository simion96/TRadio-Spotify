import pprint
import sys
import os

import spotipy
import spotipy.util as util
import json


#https://open.spotify.com/user/1118158951/playlist/4uAEvLEhJLmzPmmCkIVBHF

if len(sys.argv) > 0:
    #username = sys.argv[1]
    playlist_id = '4uAEvLEhJLmzPmmCkIVBHF'
    #track_ids = ['spotify:track:1xalXygnuN9pA9NejSHfJV', '0PO7fVyPLMShxeh9OKjbWB']
    #track_ids = sys.argv[3:]
else:
    print("Usage: %s username playlist_id track_id ..." % (sys.argv[0],))
    sys.exit()

clientID = os.getenv('SPOTIPY_CLIENT_ID')
clientSecret = os.getenv('SPOTIPY_CLIENT_SECRET')
redirect = os.getenv('SPOTIPY_REDIRECT_URI')
username = '1118158951'
spotifyusername = 'spotifydiscover'
playlist_id = '4uAEvLEhJLmzPmmCkIVBHF'

new_song_id = []
new_song_id.append("7jqPrUh6IR8nh7qM2gJyyl")
#print clientID
#print clientSecret

scope = 'playlist-modify-public'
token = util.prompt_for_user_token(username, scope, client_id = clientID, client_secret = clientSecret, redirect_uri = redirect)
#
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
        #print(song["track"]["id"])
    
    print(playlistSongs)
    
    if (new_song_id[0] not in playlistSongs):
        print ("it wasnt here")
        print (new_song_id)
        sp.user_playlist_add_tracks(username, playlist_id, new_song_id)
    
    
    # sp.user_playlist_remove_all_occurrences_of_tracks(user = username, playlist_id = playlist_id, tracks = targetCurrSongs)
    #
    # counter = 0
    # requestLimit = 0
    # requested = False;
    # for playlist in playlists:
    #     playlist = sp.user_playlist(username, playlists[counter], fields='tracks, next')
    #     playlistItems = playlist['tracks']['items']
    #     for x in playlistItems:
    #         sourceSongs.append(x['track']['uri'])
    #     counter+=1
    # print 'source uris: '
    # print sourceSongs
    #
    #
    #
    # leftover = len(sourceSongs)
    # limit = 100
    # start = 0
    # end = 99
    # iterations = len(sourceSongs) / limit +1
    # counter = 0;
    # while counter < iterations :
    #     if leftover < limit:
    #         sp.user_playlist_add_tracks(username, playlist_id, sourceSongs)
    #     else:
    #         sp.user_playlist_add_tracks(username, playlist_id, sourceSongs[start:end])
    #         start+=100
    #         end+=100
    #     counter+=1
    #         #sp.user_playlist_add_tracks(username, playlist_id, targetCurrSongs)

else:
    print("Can't get token for", username)



#spotify:track:1MsyEbEQca1sfC9JnkKnOm
#spotify:track:2ktzBAD5iGVfK1SSE2gFMk


