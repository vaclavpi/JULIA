#################################################### IMPORT POTŘEBNÝCH MODULŮ ####################################################
import os
import datetime
from fileinput import close
import webbrowser
import speech_recognition as sr
import pyttsx3
import requests
from bs4 import BeautifulSoup
import pyautogui
import Modules.Volume as Volume
import random
from email.mime import audio
from itertools import cycle
from socket import timeout
from flask import flash
from more_itertools import take
from requests import request
from pyautogui import click
from time import sleep
from cProfile import label
import wikipedia 
import smtplib
import pyjokes  
import time                                                                         
import subprocess                                                                                                                                       
import subprocess
import winshell
import smtplib
import ctypes
from random import choice
from tkinter import *
import cv2
import smtplib
import pyowm
from pyowm import OWM
from pyowm.utils import geo
from pyowm.alertapi30.enums import WeatherParametersEnum, OperatorsEnum, AlertChannelsEnum
from pyowm.alertapi30.condition import Condition
from Modules.Calculatenumbers import speak
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
#################################################### IMPORT POTŘEBNÝCH MODULŮ ####################################################
#################################################### NASTAVENÍ A PAMĚŤ SYSTÉMU ####################################################
pyautogui.press("F11")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[3].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 200) 
engine.setProperty('volume', 1.0)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

from Settings.OwnSettings import sendemail

from Settings.Settings import alarm

from Settings.Settings import get_location

from Settings.Settings import city
#################################################### NASTAVENÍ A PAMĚŤ SYSTÉMU ####################################################
#################################################### FUNKCE SYSTÉMU ####################################################
username = os.getenv('username')

from Settings.Settings import takeCommand
takeCommand()

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()

        if "julia" in query or "wake up" in query or "hello" in query or "Are you there" in query or "help" in query or "assistant" in query or "hi"in query or "good"in query:
            from Modules.Greeting import greeting
            greeting()


            while True:
                query = takeCommand().lower()

                if "go to sleep" in query:
                    speak("Ok sir, You can call me anytime!")
                    break

                elif "hello" in query or "hi" in query or "Julia" in query:
                    speak("Hello sir, how are you?")

                elif "i am fine" in query:
                    speak("That´s great, sir!")

                elif "how are you?" in query:
                    speak("Perfect, sir!")
                    speak("How are you, Sir?")

                elif "thank you" in query or "thank" in query:
                    speak("You are welcome, sir!")
                
                elif "tired" in query or "song" in query:
                    from Modules.Tired import tired
                    tired()

                elif "pause" in query or "stop" in query:
                        pyautogui.press("k")
                        speak("Video paused, sir!")

                elif "play" in query:
                    pyautogui.press("k")
                    speak("Video play, sir!")

                elif 'who is' in query:                                                         
                    query = query.replace('who is',"")                                          
                    speak(wikipedia.summary(query,2))

                elif "ip address" in query:
                    ip = requests.get('https://api.ipify.org').text
                    print(ip)
                    speak(f"Your ip address is {ip}")

                elif "window" in query:
                    from Modules.SwitchWindow import SW
                    SW()

                elif "who made you" in query or "who created you" in query:
                    speak("I have been created by Válcav Pisinger from Czech republic. His webpage is: vapi.ml")
        
                elif 'fine' in query or "good" in query:
                    speak("It's good to know that your fine")

                elif "who i am" in query:
                    speak("If you talk then definitely your human.")
        
                elif "why you came to world" in query:
                    speak("Thanks to Václav Pisinger. further It's a secret")
        
                elif "who are you" in query:
                    speak("I am your virtual assistant created by Václav Pisinger")
        
                elif 'reason for you' in query:
                    speak("I was created as a Minor project by Mister Václav Pisinger")
        
                elif 'lock window' in query:
                        speak("locking your device")
                        ctypes.windll.user32.LockWorkStation()
        
                elif 'shutdown' in query:
                    speak("Sir, are You sure you want to shutdown?")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")

                    elif shutdown == "no":
                        break
                        
                elif 'empty recycle bin' in query:
                    speak("Wait a second, sir!")
                    winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
                    speak("Recycle Bin Recycled, sir!")
        
                elif "don't listen" in query or "stop listening" in query:
                    speak("for how much time you want to stop Julia from listening commands")
                    a = int(takeCommand())
                    time.sleep(a)
                    print(a)
        
                elif "where is" in query:
                    query = query.replace("where is", "")
                    location = query
                    speak("User asked to Locate")
                    speak(location)
                    webbrowser.open("https://www.google.nl/maps/place/" + location + "")

                elif "restart" in query:
                    subprocess.call(["shutdown", "/r"])
                    
                elif "hibernate" in query or "sleep" in query:
                    speak("Hibernating")
                    subprocess.call("shutdown / h")
        
                elif "log off" in query or "sign out" in query:
                    speak("Make sure all the application are closed before sign-out")
                    time.sleep(5)
                    subprocess.call(["shutdown", "/l"])
        
                elif "new note" in query or "write a note" in query:
                    speak("What should i write, sir")
                    note = takeCommand()
                    file = open('Julia.txt', 'w')
                    speak("Sir, Should i include date and time")
                    snfm = takeCommand()
                    if 'yes' in query or 'sure' in query:
                        strTime = datetime.datetime.now().strftime("% H:% M:% S")
                        file.write(strTime)
                        file.write(" :- ")
                        file.write(note)
                    else:
                        file.write(note)
                
                elif "note" in query or "show note" in query:
                    speak("Showinkg Notes")
                    file = open("Julia.txt", "r")
                    print(file.read())
                    speak(file.read(6))
        
                elif "update" in query or "actual version" in query:
                    speak("Your system version is the most current. (Julia - best version)")
                    print("Your system version is the most current. (Julia - best version)")

                elif "Julia" in query:
                    
                    greeting()
                    speak("Julia in your service, Sir!")
        
        
                elif "what's your name" in query or "What is your name" in query:
                    speak("My friends call me Julia")
                    print("My friends call me Julia")   

                elif 'joke' in query:                                                           
                    speak(pyjokes.get_joke())
                
                elif "mute" in query:
                    pyautogui.press("k")
                    speak("Video muted, sir!")
                
                elif "voulume up" in query:
                    from Modules.Volume import volumeUp
                    speak("Turning volume up, sir!")
                    volumeUp()
                
                elif "voulume down" in query:
                    from Modules.Volume import volumeDown
                    speak("Turning volume down, sir!")
                    volumeDown()
                
                elif "open" in query:
                    from Modules.OppenApp import openappweb
                    openappweb(query)

                elif "close" in query:
                    from Modules.OppenApp import closeappweb
                    closeappweb(query)

                elif "hide all files" in query or "hide this folder" in query:
                    os.system("attrib +h /s /d")
                    speak("Sir, all the files in this folder are now hidden")

                elif "visible" in query or "make files visible" in query:
                    os.system("attrib -h /s /d")
                    speak("Sir, all the files in this folder are now visible to everyone. I hope you are taking this decision in your own peace")

                elif "alarm" or "clock" in query:
                    print("Input time example:- 10 and 10 and 10")
                    speak("Set the time")
                    a = input("Please tell the time, sir!")
                    alarm(a)
                    speak("Done, sir!")

                elif "google" in query:
                    from Modules.SearchNow import searchGoogle
                    searchGoogle(query)
                
                elif "youtube" in query:

                    from Modules.SearchNow import searchYouTube
                    searchYouTube(query)
                
                elif "wikipedia" in query:
                    from Modules.SearchNow import searchWikipedia
                    searchWikipedia(query)
                
                elif "news" in query or "paper" in query or "newspaper" in query:
                    from Modules.NewsRead import latestnews
                    latestnews()
                
                elif "calculate" in query:
                    from Modules.Calculatenumbers import WolfRamAlpha
                    from Modules.Calculatenumbers import Calc
                    query = query.replace("calculate","")
                    query = query.replace("julia","")
                    Calc(query)

                elif 'can you do for me' in query:
                    print('I can do multiple tasks for you sir.\n tell me whatever you want to perform sir')
                    speak('I can do multiple tasks for you sir. tell me whatever you want to perform sir')

                elif 'old are you' in query:
                    print("I am a little baby sir")
                    speak("I am a little baby sir")

                elif 'open media player' in query:
                    print("opening VLC media Player")  
                    speak("opening V L C media player")
                    path = "path-to\\vlc.exe"                                       #Enter valid path for vlc.exe
                    os.startfile(path)
                
                elif "whatsapp" in query:
                    from Modules.Whatsapp import sendMessage
                    sendMessage()

                elif "temperature" in query or "weather" in query:
                    owm = pyowm.OWM('apikey')               #open weather map API key
                    #current weather forecast
                    loc = owm.weather_at_place(city)
                    weather = loc.get_weather()
                    #status
                    status = weather.get_detailed_status()
                    print(f'{status} in {city}')
                    speak(f'{status} in {city}')
                    # temperature
                    temp = weather.get_temperature(unit='celsius')
                    for key,val in temp.items():
                            if key == 'temp':
                                    print(f'{val} degree celcius')
                                    speak(f"current temperature is {val} degree celcius")
                    # humidity, wind, rain, snow
                    humidity = weather.get_humidity()
                    wind = weather.get_wind()
                    print(f'{humidity} grams per cubic meter')
                    speak(f'humidity is {humidity} grams per cubic meter')
                    print(f'wind {wind}')
                    speak(f'wind {wind}')
                    # sun rise and sun set
                    sr = weather.get_sunrise_time(timeformat='iso')
                    ss = weather.get_sunset_time(timeformat='iso')
                    speak(f'SunRise time is {sr}')
                    speak(f'SunSet time is {ss}')
                    # clouds and rain
                    loc = owm.three_hours_forecast(city)
                    clouds = str(loc.will_have_clouds())
                    rain = str(loc.will_have_rain())
                    if clouds == 'True':
                            print("It may have clouds in next 5 days")
                            speak("It may have clouds in next 5 days")
                    else:
                            print("It may not have clouds in next 5 days")
                            speak("It may not have clouds in next 5 days")
                    if rain == 'True':
                            print("It may rain in next 5 days")
                            speak("It may rain in next 5 days")
                    else:
                            print("It may not rain in next 5 days")
                            speak("It may not rain in next 5 days")

                elif 'email to' in query:
                    try:
                        query = query.replace("email to", "")
                        query = query.replace(" ", "")
                        print(query)
                        print("What should I say")
                        speak('what should I say')
                        content = takeCommand()
                        to = a[query]
                        sendemail(to, content)
                        print('Email has been sent!')
                        speak('Email has been sent!')

                    except Exception as e:
                        print(e)
                        print("Sorry Sir! I was not able to send this email")
                        speak('Sorry Sir! I was not able to send this email')

                elif 'record video' in query:
                    cap = cv2.VideoCapture(0)
                    out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*"MJPG"), 30,(640,480))
                    while(cap.isOpened()):
                        ret, frame = cap.read()
                        if ret:
                            
                            out.write(frame)

                            cv2.imshow('frame',frame)
                            if cv2.waitKey(1) & 0xFF == ord('q'):
                                break
                        else:
                            break
                    cap.release()
                    out.release()
                            
                
                elif "time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Sir, the time is {strTime}")
                
                elif "remember that" in query:
                    rememberMessage = query.replace("remeber that","")
                    rememberMessage = query.replace("julia","")
                    speak("You told me to remember that" + rememberMessage)
                    remember = open("Remember.txt","w")
                    remember.write(rememberMessage)
                    remember.close()
                
                elif "what do you remember" in query or "show remember" in query:
                    remember = open("Remember.txt","r")
                    speak("You told me" + remember.read())
                
                elif "shut down the system" in query:
                    speak("Are You sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")

                    elif shutdown == "no":
                        break
            
                
                elif "goodbye" in query or "offline" in query or "bye" in query or "exit" in query or "finally sleep" in query:
                    speak("Alright sir, going offline. It was nice working with you")
                    exit()
                    pyautogui.press("k")
#################################################### FUNKCE SYSTÉMU ####################################################