#region Imports
import speech_recognition as sr
import pyttsx3
# OS for launching apps
import os
import subprocess as sp
# Spotify Api
import json
import spotipy
import webbrowser
from SpotifyKeys import spotname , spotID , spotSecret , spotredirectURI
#URLLIB / regex
import urllib.request
import re
#PYTHON FILES with functions
from appManagement import appSelect , appClose
#endregion imports

#region spotify info
username = spotname
clientID = spotID
clientSecret = spotSecret
redirectURI = spotredirectURI

oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirectURI)
token_dict = oauth_object.get_cached_token()
token = token_dict['access_token']
spotifyObject = spotipy.Spotify(auth=token)
user = spotifyObject.current_user()
#endregion

listener = sr.Recognizer()
engine = pyttsx3.init()

    
    
def task(text):
    print('running task')
    if 'spotify' in text:
        songSelect(text)
    if 'youtube' in text:
        tubeOpen(text)
    if 'open' in text:
        appSelect(text)
    if 'close' in text:
        appClose(text)
    if 'donkey' in text:
        print('im a donkey')
    else:
        print('I Dont Understand')
            



            
def songSelect(text):
    print('running spotify song select')
    playIndex = text.find('play') + 4
    print(playIndex)
    song = text[playIndex:99]
    print(song)
    # Get the Song Name.
    searchQuery = song
    # Search for the Song.
    searchResults = spotifyObject.search(searchQuery,1,0,"track")
    # Get required data from JSON response.
    tracks_dict = searchResults['tracks']
    tracks_items = tracks_dict['items']
    song = tracks_items[0]['external_urls']['spotify']
    # Open the Song in Web Browser
    webbrowser.open(song)

def tubeOpen(text):
    print('running webopen')
    tubeIndex = text.find('play') + 4
    searchKeywords = text[tubeIndex:99].replace(' ', '_')
    print(searchKeywords)
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + searchKeywords)
    videoIds = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    webbrowser.open('https://www.youtube.com/watch?v=' + videoIds[0])
    

def startAssistant():
    engine.say('Start')
    try:
        with sr.Microphone() as source:
            #engine.say('How can I help you?')
            #print('listening...')
            #voice = listener.listen(source)
            #command = listener.recognize_google(voice)
            #command = command.lower()
            #print(command)
            tempCommand = 'juice open valorant'
            print(tempCommand)
            if 'juice' in tempCommand:
                task(tempCommand)
                #task(command)
                
    except:
        pass
    
startAssistant()