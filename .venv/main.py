#region Imports
import speech_recognition as sr
import pyttsx3
import pywhatkit
from decouple import config
# OS for launching apps
import os
import subprocess as sp
import win32gui
import webbrowser
import datetime
#URLLIB / regex
import urllib.request
import re
#PYTHON FILES with functions
from appManagement import appOpen , appClose , appFocus
#endregion imports


listener = sr.Recognizer()
engine = pyttsx3.init()
engine.runAndWait()
es = engine.say
erw = engine.runAndWait()
    
    
def task(text):
    print('running task')
    if 'play' in text:
        youtube(text)
    if 'open' in text:
        appOpen(text)
    if 'close' in text:
        appClose(text)
    if 'focus' in text:
        appFocus(text)
    if 'donkey' in text:
        print('im a donkey')
        engine.say('I, am a donkey')
        engine.runAndWait()


def youtube(text):
    print('running Youtube')
    tubeIndex = text.find('play') + 4
    searchKeywords = text[tubeIndex:99].replace(' ', '_')
    print(searchKeywords)
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + searchKeywords)
    videoIds = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    webbrowser.open('https://www.youtube.com/watch?v=' + videoIds[0])
    

def startAssistant():
    try:
        with sr.Microphone() as source:
            engine.say("How may i help you?")
            engine.runAndWait()
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
            #tempCommand = 'juice open discord'
            #print(tempCommand)
            if 'jimmy' in command:
                command = command.replace('jimmy ', '')
                print(command)
                #task(tempCommand)
                task(command)
                
    except:
        pass
    
def run():
    startAssistant()
run()