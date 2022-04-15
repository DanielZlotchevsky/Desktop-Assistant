import os
import subprocess as sp
import pyttsx3

engine = pyttsx3.init()

def appSelect(text):
    print('running appSelect')
    if 'league of legends' in text:
        sp.Popen('C:\Riot Games\League of Legends\LeagueClient.exe')
        engine.say('Opening League of legends')
        print('league was found')
    if 'valorant' in text:
        sp.Popen('C:\Riot Games\VALORANT\live\VALORANT.exe')
        engine.say('Opening valorant')
        print('Valo was found')
    if 'blits' in text:
        sp.Popen('C:\\Users\\danje\\AppData\\Local\\Programs\\Blitz\\Blitz.exe')
        engine.say('Opening Blitz')
        print('blitz was found')
    if 'chroma' in text:
        sp.Popen('D:\Program Files (x86)\SteamLibrary\steamapps\common\ChromaChronicles\ChromaChronicles.exe')
        engine.say('Opening Chromo Chronicles')
        print('Chroma was found')