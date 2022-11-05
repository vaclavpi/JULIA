import datetime
import os
import requests
import speech_recognition as sr
from Modules.Calculatenumbers import speak

username = os.getenv('username')

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
MONTHS = ["january", "february", "march", "april", "may", "june","july", "august", "september","october","november", "december"]
DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
DAY_EXTENTIONS = ["rd", "th", "st", "nd"]

def alarm(query):
    timehere = open("AlarmText.txt", "a")
    timehere.write(query)
    timehere.close()
    os.startfile("Alarm.py")

def get_location():
    #Function To Print GeoIP Latitude & Longitude#
    ip_request = requests.get('https://get.geojs.io/v1/ip.json')
    my_ip = ip_request.json()['ip']
    geo_request = requests.get('https://get.geojs.io/v1/ip/geo/' +my_ip + '.json')
    geo_data = geo_request.json()
    geo = geo_data['city']
    return geo


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.energy_threshold = 300
        print("Listening...")
        audio = r.listen(source,0,4)

    try: 
        query = r.recognize_google(audio, language='en')
        print(f"{username}: {query}")

    except Exception as e:
        print("Znovu prosim")
        return "None"
    return query


def city():
    while True:
        city=get_location()
        if city=="Puducherry":
            speak("You are in Puducherry")
        else:
            speak(f"You are in {city}")
            speak(f"You are in {city}. Go to Puducherry first.")
            continue
        query = takeCommand().lower()
        if 'exit' in query:
            speak("Bye {username}!")
            break
