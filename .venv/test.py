import win32gui
import pyttsx3
import re

engine = pyttsx3.init()
es = engine.say
erw = engine.runAndWait()

def window_enum_handler(hwnd, resultList):
    if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) != '':
        resultList.append((hwnd, win32gui.GetWindowText(hwnd)))

def get_app_list(handles=[]):
    mlst=[]
    win32gui.EnumWindows(window_enum_handler, handles)
    for handle in handles:
        mlst.append(handle)
    return mlst

appwindows = get_app_list()
for i in appwindows:
    print(i)
    
hand = win32gui.FindWindow(None, 'VALORANT  ')
print('here: ' + str(hand))

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
            'window': 'FTL: Faster Than Light'
        },
    }
}

