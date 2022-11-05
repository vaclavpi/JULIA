import datetime
import os

def alarm(query):
    timehere = open("AlarmText.txt", "a")
    timehere.write(query)
    timehere.close()
    os.startfile("Alarm.py")