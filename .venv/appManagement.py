from ctypes.wintypes import HWND
import os
import subprocess as sp
import pyttsx3
import win32gui


engine = pyttsx3.init()
es = engine.say
erw = engine.runAndWait()


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
        os.popen('C:\\Users\\danje\AppData\\Local\Discord\\app-1.0.9004\\Discord.exe')
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