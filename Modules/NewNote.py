import pyttsx3
import speech_recognition as sr
import datetime
from Settings.Settings import takeCommand
import Settings.Settings as Settings


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

r = sr.Recognizer()
source = sr.Microphone
audio = r.listen(source,0,4)
query = r.recognize_google(audio, language='en-GB')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 190) 
engine.setProperty('volume', 1.0)


def NewNote():
    speak("What should i write, sir")
    note = takeCommand()
    file = open('Jarvis.txt', 'w')
    speak("Sir, Should i include date and time")
    snfm = takeCommand()
    if 'yes' in query or 'sure' in query:
        strTime = datetime.datetime.now().strftime("% H:% M:% S")
        file.write(strTime)
        file.write(" :- ")
        file.write(note)
    else:
        file.write(note)