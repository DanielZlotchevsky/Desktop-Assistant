import os
import subprocess as sp
import pyttsx3

engine = pyttsx3.init()

def appSelect(text):
    print(text)
    print('running appSelect')
    if 'league' and 'legends' in text:
        os.popen('C:\Riot Games\League of Legends\LeagueClient.exe')
        engine.say('Opening League of legends')
        print('league was found')
    if 'valorant' in text:
        print('Valo was found')
        sp.run('C:\\Riot Games\\VALORANT\\live\\VALORANT.exe')
        engine.say('Opening valorant')
        print('Valo was found')
    if 'blitz' in text:
        os.popen('C:\\Users\\danje\\AppData\\Local\\Programs\\Blitz\\Blitz.exe')
        engine.say('Opening Blitz')
        print('blitz was found')
    if 'chroma' in text:
        os.popen('D:\Program Files (x86)\SteamLibrary\steamapps\common\ChromaChronicles\ChromaChronicles.exe')
        engine.say('Opening Chromo Chronicles')
        print('Chroma was found')
    if 'rocket league' in text:    
        sp.run('D:\\Program Files (x86)\\Epic Games\\rocketleague\\Binaries\\Win64\\RocketLeague.exe')
        print('Rocket league was found')




def appClose(text):
    print('running app close')
    if 'league' and 'legends' in text:
        os.system('taskkill /F /im LeagueClient.exe')
        print('league was closed')
    if 'valorant' in text:
        os.system('taskkill /F /im VALORANT.exe')
        print('Valo was closed')
    if 'blitz' in text:
        os.system('taskkill /F /im Blitz.exe')
        print('blitz was closed')
    if 'chroma' in text:
        os.system('taskkill /F /im ChromaChronicles.exe')
        print('Chroma was closed')
    if 'rocket league' in text:    
        os.system('taskkill /F /im RocketLeague.exe')
        print('Rocket league was closed')



def appFocus(text):
    print('running appFocus')
    if 'league' and 'legends' in text:
        focus = 'League of Legends'
        os.system('taskkill /F /im LeagueClient.exe')
        print('league in focus')
    if 'valorant' in text:
        focus = ''
        os.system('taskkill /F /im VALORANT.exe')
        print('Valo was closed')
    if 'blitz' in text:
        focus = 'Blitz'
        os.system('taskkill /F /im Blitz.exe')
        print('blitz in focusin focus')
    if 'chroma' in text:
        focus = 'ChromaChronicles'
        os.system('taskkill /F /im ChromaChronicles.exe')
        print('Chroma in focus')
    if 'rocket league' in text:
        focus = 'Rocket League (64-bit, DX11, Cooked)'
        os.system('taskkill /F /im RocketLeague.exe')
        print('Rocket league in focus')