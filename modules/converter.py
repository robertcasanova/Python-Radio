import os
from subprocess import call
import urllib2
import json


def convertToFlac(filename):
	filename = filename.split('.')[0]
	if not os.path.exists(filename+".flac"):
		call(["flac "+filename+".wav", "--sample-rate=16000"],shell=True)
		return True
	else:
		os.remove(filename+".flac")
		convertToFlac(filename)
		

def convertFlacToTxt(filename):
	f = open(filename, 'r')
	data = f.read()
	f.close()

	#make a google API request
	req = urllib2.Request('https://www.google.com/speech-api/v1/recognize?xjerr=1&client=chromium&pfilter=2&lang=en-US&maxresults=1')
	req.add_header('Content-type', 'audio/x-flac; rate=16000')
	req.add_data(data)
	res = urllib2.urlopen(req)

	obj = json.loads(res.read())
	title =  obj['hypotheses'][0]['utterance']
	return title

	

