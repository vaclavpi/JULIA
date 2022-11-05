import os
import pyautogui
import webbrowser
import pyttsx3
from time import sleep

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 190) 
engine.setProperty('volume', 1.0)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


OppenApp = {"commandprompt":"cmd","paint":"paint","word":"winword","excel":"excel","chrome":"chrome","vscode":"code","powerpoit":"powerpoint","youtube":"youtube","whatsapp":"whatsapp","instagram":"instagram","facebook":"facebook","notepad":"notepad","mail":"mail"}

def openappweb(query):
    speak("App is lainching, sir!")
    if ".com" in query or ".org" in query or ".cz" in query:
        query = query.replace("open","")
        webbrowser.open(f"https://www.{query}")
    else:
        keys = list(OppenApp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {OppenApp[app]}")

def closeappweb(query):
    speak("Closing, sir!")
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl","w")

    elif "two tab" in query or "2 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("All tabs closed, sir!")

    elif "three tab" in query or "3 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("All tabs closed, sir!")

    elif "four tab" in query or "4 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("All tabs closed, sir!")    

    elif "five tab" in query or "5 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("All tabs closed, sir!")         

    elif "six tab" in query or "6 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("All tabs closed, sir!")  

    else:
        keys = list(OppenApp.keyss())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {OppenApp[app]}.exe")