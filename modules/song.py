import urllib2
import json



def getSongUrl(title):
    title = urllib2.quote(title, '')
    print(title);
    req = urllib2.Request('http://developer.echonest.com/api/v4/song/search?api_key=KCRLAIJYTRP8SA7V0&format=json&results=1&title='+title+'&sort=song_hotttnesss-desc&bucket=id:7digital-US&bucket=tracks')
    res = urllib2.urlopen(req)
    obj = json.loads(res.read())
    print obj['response']['songs'][0]['artist_name']
    return obj['response']['songs'][0]['tracks'][0]['preview_url']

def download(url, filename):
	webFile = urllib2.urlopen(url)
	localFile = open(filename, 'w')
	localFile.write(webFile.read())
	webFile.close()
	localFile.close()    