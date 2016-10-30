from radio import Radio
from time import sleep
from spotify import Spotify

_spotify = Spotify()
id = _spotify.getSongID("the definition of a rap flow")
songs = _spotify.getPlaylistSongs()
_spotify.addSongs(songs, id)

#_radio = Radio()
#song = _radio.getCurrentSong()
#sleep(5)
#print(song)
#_radio.closeBrowser()