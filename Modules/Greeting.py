import imp
import pyttsx3
import datetime
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[3].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 190) 
engine.setProperty('volume', 1.0)


username = os.getenv('username')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

strTime = datetime.datetime.now().strftime("%H:%M")


def greeting():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak(f"Good Morning sir! All systems will be prepared in a few minutes. It´s {strTime}")


    elif hour>=12 and hour<18:
        speak(f"Good afternoon sir! All systems will be prepared in a few minutes. It´s {strTime}")   

    else:
        speak(f"Good evening sir! All systems will be prepared in a few minutes. It´s {strTime}")  
    