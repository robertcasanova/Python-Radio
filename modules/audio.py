import pyaudio
import wave
import sys
from subprocess import call
from time import sleep

p = pyaudio.PyAudio()
p_read = p

options = {
    'chunk' : 1024,
    'format': pyaudio.paInt16,
    'channels': 1,
    'rate' : 16000
}

#
# TODO: set a trashold for start recording    
#
def record(length,file):
    p = pyaudio.PyAudio()
    stream = p.open(format = options['format'],
                    channels = options['channels'],
                    rate = options['rate'],
                    input = True,
                    frames_per_buffer = options['chunk'])
    print "Start Recording"
    all = []
    for i in range(0, options['rate']/options['chunk']*length):
        data = stream.read(options['chunk'])
        all.append(data)
    print "End Recording"
    stream.close()
    p.terminate()
    data = ''.join(all)
    __saveAudioDataToFile(data,file)

def play(filename):
    p_read = pyaudio.PyAudio()
    wf = wave.open(filename,'rb')
    stream = p.open(format = p_read.get_format_from_width(wf.getsampwidth()),
                    channels = wf.getnchannels(),
                    rate = wf.getframerate(),
                    output = True)
    data = wf.readframes(options['chunk'])
    while data != '':
        stream.write(data)
        data = wf.readframes(options['chunk'])


    stream.close()
    p_read.terminate()

def play_ext(filename):
    call(["afplay "+filename],shell=True)


def __saveAudioDataToFile(data,filename):
    wf = wave.open(filename, 'wb')
    wf.setnchannels(options['channels'])
    wf.setsampwidth(p.get_sample_size(options['format']))
    wf.setframerate(options['rate'])
    wf.writeframes(data)
    wf.close()
