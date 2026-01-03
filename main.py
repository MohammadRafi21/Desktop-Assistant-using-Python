import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia 
import webbrowser
import os


# Taking voice from my system
engine = pyttsx3.init('sapi5') # to access the voice property in the system we have to use 'sapi5'
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
#print(voices[0].id)
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate', 150)

# speak function

def speak(text):
    """
    Docstring for speak
    it takes text and return voice
    
    :param text: the text take string data type
    """
    engine.say(text)
    engine.runAndWait()

speak("Hello I am a programmer, How are you?")

# 
