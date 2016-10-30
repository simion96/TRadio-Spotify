from radio import Radio
from time import sleep

_radio = Radio()
song = _radio.getCurrentSong()
sleep(5)
print(song)
_radio.closeBrowser()