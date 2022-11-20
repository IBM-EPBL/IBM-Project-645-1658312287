import speech_recognition as sr
from os import walk

r = sr.Recognizer()
#optional
#r.energy_threshold = 300

def startConvertion(path = 'file.wav', lang = 'en-IN'): 
    with sr.AudioFile(path) as source:
        #print('Fetching File')
        audio_file = r.record(source)
        print(r.recognize_google(audio_file, language=lang))
startConvertion()