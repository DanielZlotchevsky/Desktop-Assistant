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
#URLLIB / regex
import urllib.request
import re
#imports for other files with functions
from appSelect import appSelect
#endregion imports

#region spotify info
username = '12138504689'
clientID = '1105e3e91a5a462c941d28022dc4fac7'
clientSecret = '58e2d61b5a3a4f1883eb0a66c89b57bc'
redirectURI = 'http://google.com/'


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
        webOpen(text)
    if 'open' in text:
        appSelect(text)
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

def webOpen(text):
    print('running webopen')


        

def startAssistant():
    engine.say('Start')
    try:
        with sr.Microphone() as source:
            #engine.say('How can I help you?')
            #print('listening...')
            #voice = listener.listen(source)
            #command = listener.recognize_google(voice)
            #command = command.lower()
            tempCommand = 'juice play moo by doja cat'
            print(tempCommand)
            if 'juice' in tempCommand:
                task(tempCommand)
                #task(command)
                
    except:
        pass
    
startAssistant()