import random
import webbrowser
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[3].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 190) 
engine.setProperty('volume', 1.0)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def tired():
    speak("Play your favorite songs, sir!")
    a = (1,2,3,4,5)
    b = random.choice(a)
    if b==1:
        webbrowser.open("https://www.youtube.com/watch?v=hT_nvWreIhg")
    elif b==2:
        webbrowser.open("https://www.youtube.com/watch?v=ktvTqknDobU")
    elif b==3:
        webbrowser.open("https://www.youtube.com/watch?v=uJ_1HMAGb4k")
    elif b==4:
        webbrowser.open("https://www.youtube.com/watch?v=qP-7GNoDJ5c")
    elif b==5:
        webbrowser.open("https://www.youtube.com/watch?v=7wtfhZwyrcc")