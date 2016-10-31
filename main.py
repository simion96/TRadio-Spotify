from radio import Radio
from time import sleep
from spotify import Spotify

_radio = Radio()
_spotify = Spotify()
#songName = _radio.getCurrentSong()
#id = _spotify.getSongID(songName)
#sourceSongs = _spotify.getPlaylistSongs()
#_spotify.addSongs(sourceSongs, id)

while True:
	try:
		songName = _radio.getCurrentSong()
		id = _spotify.getSongID(songName)
		sourceSongs = _spotify.getPlaylistSongs()
		_spotify.addSongs(sourceSongs, id)
		_radio.closeBrowser()
		sleep(120)
	except Exception as e:
		print("failed to add song {} . {}".format(songName, str(e))) 		
		pass

#print (_radio.checkSongName("Alabama Shakes - Future People (Official Video - Live from Capitol Studio A) --- Alabama Shakes - Future People (Official Video - Live from Capitol Studio A)"))
#_radio = Radio()
#song = _radio.getCurrentSong()
#sleep(5)
#print(song)
#_radio.closeBrowser()
