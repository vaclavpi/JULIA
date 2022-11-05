from unittest import result
import speech_recognition as sr
import pyttsx3
import pywhatkit
from textblob import Sentence
import wikipedia
import webbrowser
import pyowm


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Jarvis: Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)
    try:
        print("Understanding...")    
        query = r.recognize_google(audio, language='en-US')
        print(f"Sir: {query}\n")

    except Exception as e:
        print("JULIA: Say that again please!")  
        return "None"
    return query

query = takeCommand().lower()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 190) 
engine.setProperty('volume', 1.0)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("google","")     
        query = query.replace("google search","")
        query = query.replace("julia","")                                                                                
        speak(f'Here is what I found for {query} on google, sir!')

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,1)
            speak(result)

        except:
            speak("No speakable output avilable, sir!")


def searchYouTube(query):
    if "youtube" in query:
        speak("This is what I found for your search, sir!")
        query = query.replace("youtube search","") 
        query = query.replace("youtube","") 
        query = query.replace("julia","") 
        web = f"https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done, sir!")

def searchWikipedia(query):
    if "wikipedia" in query:
        speak("searching wikipedia")
        query = query.replace("according to wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to wikipedia")
        speak(results)
        print(result)
        