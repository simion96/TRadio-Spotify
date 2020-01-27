from radio import Radio
from time import sleep
from spotify import Spotify
import utils as utils

_radio = Radio()
_spotify = Spotify()

while True:
	try:
		songName = _radio.getCurrentSong()
		id = _spotify.getSongID(songName)
		if (id != ""):
			utils.write_file("songsUnrecognised.txt", songName)
		sourceSongs = _spotify.getPlaylistSongs()
		_spotify.addSongs(sourceSongs, id)
		_radio.closeBrowser()
		sleep(120)
	except Exception as e:
		utils.write_file("songsFailed.txt", songName)
		utils.write_file("exceptions.txt", str(e)) 		
		pass