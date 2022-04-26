from ctypes.wintypes import HWND
import os
import re
import subprocess as sp
import pyttsx3
import win32gui


engine = pyttsx3.init()
es = engine.say
erw = engine.runAndWait()

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
        'Apex': {
            'name': 'Apex Legends',
            'path': 'D:\\Program Files (x86)\\Epic Games\\Fortnite\\Binaries\\Win64\\Fortnite.exe',
            'exe': 'Fortnite.exe',
            'window': 'Fortnite  '
    }
}

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

def appOpen(text):
    print(text)
    print('running appSelect')
    if 'league' in text:
        os.popen('C:\Riot Games\League of Legends\LeagueClient.exe')
        es('league was opened')
        engine.runAndWait()
    if 'valorant' in text:
        print('Valo was opened')
        os.startfile(r'C:\\Users\\Public\\Desktop\\VALORANT.lnk')
        es('Valo was opened')
        engine.runAndWait()
    if 'blitz' in text:
        os.popen('C:\\Users\\danje\\AppData\\Local\\Programs\\Blitz\\Blitz.exe')
        es('blitz was opened')
        engine.runAndWait()
    if 'chroma' in text:
        os.popen('D:\Program Files (x86)\SteamLibrary\steamapps\common\ChromaChronicles\ChromaChronicles.exe')
        es('Chroma was opened')
        engine.runAndWait()
    if 'rocket' in text:    
        sp.run('D:\\Program Files (x86)\\Epic Games\\rocketleague\\Binaries\\Win64\\RocketLeague.exe')
        es('Rocket league was opened')
        engine.runAndWait()
    if 'discord' in text: 
        sp.Popen('C:\\Users\\danje\\AppData\\Local\Discord\\app-1.0.9004\\Discord.exe')
        es('Disc was opened')
        engine.runAndWait()

def appClose(text):
    print('running app close')
    if 'league' in text:
        os.system('taskkill /F /im LeagueClient.exe')
        es('league was closed')
        engine.runAndWait()
    if 'valorant' in text:
        os.system('taskkill /F /im VALORANT.exe')
        es('Valo was closed')
        engine.runAndWait()
    if 'blitz' in text:
        os.system('taskkill /F /im Blitz.exe')
        es('blitz was closed')
        engine.runAndWait()
    if 'chroma' in text:
        os.system('taskkill /F /im ChromaChronicles.exe')
        es('Chroma was closed')
        engine.runAndWait()
    if 'rocket' in text:    
        os.system('taskkill /F /im RocketLeague.exe')
        es('Rocket league was closed')
        engine.runAndWait()
    if 'discord' in text:
        os.system('taskkill /F /im Discord.exe')
        es('Discord was closed')
        engine.runAndWait()



def appFocus(text):
    print('running appFocus')
    if 'league' in text:
        hwnd = win32gui.FindWindow(None, 'League of Legends')
        print(hwnd)
        win32gui.ShowWindow(hwnd, 6)
        win32gui.ShowWindow(hwnd, 9)
        es('League is in focus')
        engine.runAndWait()
    if 'valorant' in text:
        hwnd = win32gui.FindWindow(None, 'VALORANT  ')
        win32gui.ShowWindow(hwnd, 6)
        win32gui.ShowWindow(hwnd, 9)
        es('Valo is in focus')
        engine.runAndWait()
    if 'blitz' in text:
        hwnd = win32gui.FindWindow(None, 'Blitz')
        win32gui.ShowWindow(hwnd, 6)
        win32gui.ShowWindow(hwnd, 9)
        es('blitz is in focus')
        engine.runAndWait()
    if 'chroma' in text:
        hwnd = win32gui.FindWindow(None, 'ChromaChronicles')
        win32gui.ShowWindow(hwnd, 6)
        win32gui.ShowWindow(hwnd, 9)
        es('Chroma in is focus')
        engine.runAndWait()
    if 'rocket' in text:
        hwnd = win32gui.FindWindow(None, 'Rocket League (64-bit, DX11, Cooked)')
        win32gui.ShowWindow(hwnd, 6)
        win32gui.ShowWindow(hwnd, 9)
        es('Rocket league is in focus')
        engine.runAndWait()
    if 'discord' in text:
        hwnd = win32gui.FindWindow(None, 'Discord')
        win32gui.ShowWindow(hwnd, 6)
        win32gui.ShowWindow(hwnd, 9)
        es('Discord is in focus')
        engine.runAndWait()