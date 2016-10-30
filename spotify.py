import pprint
import sys
import os

import spotipy
import spotipy.util as util
import json

class Spotify:
    def __init__(self):
        self.clientID = os.getenv('SPOTIPY_CLIENT_ID')
        self.clientSecret = os.getenv('SPOTIPY_CLIENT_SECRET')
        self.redirect = os.getenv('SPOTIPY_REDIRECT_URI')
        self.username = '1118158951'
        self.spotifyusername = 'spotifydiscover'
        self.playlist_id = '4uAEvLEhJLmzPmmCkIVBHF'
        self.new_song_id = "7jqPrUh6IR8nh7qM2gJyyl"
        self.scope = "playlist-modify-public"
        self.token = util.prompt_for_user_token(self.username, self.scope, client_id = self.clientID, client_secret = self.clientSecret, redirect_uri = self.redirect)
        #try:
        #    self.token = util.prompt_for_user_token(self.username, self.scope, client_id = self.clientID, client_secret = self.clientSecret, redirect_uri = self.redirect)
        #except Exception as e:
        #    print("MEssage:" +e)
        #    print("e args" + e.args)
        #if (self.token):
        #    raise Exception("the authentication token is empty")
        self.sp = spotipy.Spotify(auth=self.token)
        self.sp.trace = False
        
        
    def getSongID(self, term, limit = 10, type = "track"):
        search = self.sp.search(term)
        results = ""
        if not (search["tracks"]["total"] == 0):
            results = search["tracks"]["items"][0]["external_urls"]["spotify"][31:]
        return results
        
    
    def getPlaylistSongs(self, playlist_id = None, fields="tracks, next"):
        if (playlist_id != None):
            self.playlist_id = playlist_id
        playlistSongs = []
        playlistResults = self.sp.user_playlist(self.username, self.playlist_id, fields)
        for song in playlistResults["tracks"]["items"]:
            playlistSongs.append(song["track"]["id"])
        
        return playlistSongs
    
    def addSongs(self, source, new_song):
        if (new_song != "" and source != ""):
            if (new_song not in source):
                self.sp.user_playlist_add_tracks(self.username, self.playlist_id, [new_song])
#https://open.spotify.com/user/1118158951/playlist/4uAEvLEhJLmzPmmCkIVBHF