#-------------------------------------Imports and Declarations----------------------------------------#


#region Imports


import speech_recognition as sr
import pyttsx3
# OS for launching apps
import os
import subprocess as sp
import sys
import win32gui
import webbrowser
import datetime
import keyboard
#URLLIB / regex
import urllib.request
import re


#endregion imports

#region TTS engine and declarations


engine = pyttsx3.init()
engine.runAndWait()
es = engine.say
erw = engine.runAndWait()


#endregion

#region APPS LIBRARY
apps = {
    "app": {
        'league': {
            'name': 'League',
            'path': 'C:\Riot Games\League of Legends\LeagueClient.exe',
            'exe': 'LeagueClient.exe',
            'window': 'League of Legends'
        },
        
        'valorant': {
            'name': 'Valorant',
            'path': r'C:\\Users\\Public\\Desktop\\VALORANT.lnk',
            'exe': 'VALORANT.exe',
            'window': 'VALORANT  '
        },
        
        'blitz': {
            'name': 'Blitz',
            'path': 'C:\\Users\\danje\\AppData\\Local\\Programs\\Blitz\\Blitz.exe',
            'exe': 'Blitz.exe',
            'window': 'Blitz'
        },
        
        'chroma': {
            'name': 'Chroma',
            'path': 'D:\Program Files (x86)\SteamLibrary\steamapps\common\ChromaChronicles\ChromaChronicles.exe',
            'exe': 'ChromaChronicles.exe',
            'window': 'ChromaChronicles'
        },
        
        'rocket': {
            'name': 'Rocket League',
            'path': 'D:\\Program Files (x86)\\Epic Games\\rocketleague\\Binaries\\Win64\\RocketLeague.exe',
            'exe': 'RocketLeague.exe',
            'window': 'Rocket League (64-bit, DX11, Cooked)' 
        },
        
        'discord': {
            'name': 'Discord',
            'path': 'C:\\Users\\danje\\AppData\\Local\Discord\\app-1.0.9004\\Discord.exe',
            'exe': 'Discord.exe',
            'window': 'Discord'
        },
        
        'fortnite': {
            'name': 'Fortnite',
            'path': 'D:\\Program Files (x86)\\Epic Games\\Fortnite\\Binaries\\Win64\\Fortnite.exe',
            'exe': 'Fortnite.exe',
            'window': 'Fortnite  '
        },
    
        'apex': {
            'name': 'Apex Legends',
            'path': 'E:\\Program FIles(x86)\\Origin Games\\Apex\\r5apex.exe',
            'exe': 'r5apex.exe',
            'window': 'Apex'
        },
        
        'faster': {
            'name': 'FTL',
            'path': 'D:\\Program Files (x86)\\SteamLibrary\\steamapps\\common\\FTL Faster Than Light\\FTLGame.exe',
            'exe': 'FTLGame.exe',
            'window': 'FTL: Faster Than Light'
        },
    }
}


#endregion


#-----------------------------------------Code--------------------------------------------#


#region Task Determine


def task(text):
    print('running task')
    if 'play' in text:
        youtube(text)
    if 'open' in text:
        key = 'open'
        getApp(text, key)
    if 'turn off' in text:
        key = 'close'
        getApp(text, key)
    if 'focus' in text:
        key = 'focus'
        getApp(text, key)
    if 'donkey' in text:
        print('im a donkey')
        engine.say('I, am a donkey')
        engine.runAndWait()
    if 'terminate' in text:
        os._exit(1)
        
        
#endregion

#region Application functions


def getApp(text, key):
    print('running getApp')
    print('Key and text' + key, text)
    for x in apps['app']:
        if x in text:
            y = apps['app'][x]
            if key == 'open':
                APPOPEN(y['name'], y['path'].replace('\\','\\' ))
            if key == 'close':
                APPCLOSE(y['name'], y['exe'])
            if key == 'focus':
                APPFOCUS(y['name'], y['window'])


def APPOPEN(name, path):
    print('running APPOPEN')
    os.popen(path)
    es(name + 'was opened')
    engine.runAndWait()


def APPCLOSE(name, exe):
    print('running APPCLOSE')
    os.system('taskkill /F /im ' + exe)
    es(name + 'was closed')
    engine.runAndWait()


def APPFOCUS(name, window):
    print('running APPFOCUS')
    hwnd = win32gui.FindWindow(None, window)
    print(hwnd)
    win32gui.ShowWindow(hwnd, 6)
    win32gui.ShowWindow(hwnd, 9)
    es(name + ' is in focus')
    engine.runAndWait()



#endregion

#region Youtube search


def youtube(text):
    print('running Youtube')
    tubeIndex = text.find('play') + 4
    searchKeywords = text[tubeIndex:99].replace(' ', '_')
    print(searchKeywords)
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + searchKeywords)
    videoIds = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    webbrowser.open('https://www.youtube.com/watch?v=' + videoIds[0])


#endregion



#-------------------------------------Running the program----------------------------------------#


#region Running the app assistant

def startAssistant():
  listener = sr.Recognizer()
  with sr.Microphone() as source:
    voice = listener.listen(source)
    command = ''
    try:
      print('...')
      command = listener.recognize_google(voice)
      command = command.lower()
      print(command)
      if 'jimmy' in command:
          print(command)
          command = command.replace('jimmy ', '')
          print(command)
          task(command)
          
    except:
      pass


while True: startAssistant()

#endregion

#region Testing if microphone not working/ cannot be used

def testRun():
    print('test oof')
    try:
        tempCommand = 'jimmy open spotify'
        print(tempCommand)
        if 'jimmy' in tempCommand:
            tempCommand = tempCommand.replace('jimmy ', '')
            task(tempCommand)
    except:
        pass
#testRun()

#endregion
