from modules.audio import *
from modules.converter import *
from modules.song import *

while (1) :
	play('sounds/audio1.wav')
	print "What's your favourite song?"
	record(4,"temp.wav")
	convertToFlac("temp.wav")
	try:
		title = convertFlacToTxt("temp.flac")
	except:
		play('sounds/audio3.wav')
		print "Can you repeat please?"
		continue
	try:
		url_preview = getSongUrl(title)
		download(url_preview,"temp.mp3")
		play_ext("temp.mp3")
	except:
		play('sounds/audio2.wav')
		print "No song found"
		continue	
	