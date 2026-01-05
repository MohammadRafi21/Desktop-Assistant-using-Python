import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia 
import webbrowser
import os
import time


# Taking voice from my system
engine = pyttsx3.init('sapi5') # to access the voice property in the system we have to use 'sapi5'
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
#print(voices[0].id)
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate', 150)

# speak function

def speak(text):
    """
    Docstring for speak
    it takes text and return voice
    
    :param text: the text take string data type
    """
    engine.stop()
    engine.say(text)
    engine.runAndWait()

#speak("Hello I am a programmer, How are you?")

# speech recognition function
def takeCommand():
    """
    Docstring for takeCommand
    this function will recognize voice and return text
    """ 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..........")
        r.pause_threshold = 1
        audio = r.listen(source) # this is using google api converting voice to text

        try:
            print("Recognizing...........")
            query = r.recognize_google(audio, language = 'en-in')
            print(f"user said: {query}\n")
        except Exception as e:
            print("Say that again please.......")
            return "None"
        return query
    
#takeCommand()
# text = takeCommand()
# speak(text)

def wish_me():
    hour = (datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning sir. How are you doing?")
    
    elif hour>=12 and hour<18:
        speak("Good afternoon sir. How are you doing?")

    else:
        speak("Good evening sir. How are you doing?")
    
    speak("I am Friday. Tell me sir how can i help you?")


if __name__ == "__main__":

    wish_me()
    time.sleep(1)

    while True:

        query = takeCommand().lower()


        if "wikipedia" in query:
            speak("Searching wikipedia")
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query, sentences = 2)
            time.sleep(0.5)
            speak("According to wikipedia")
            print(results)
            time.sleep(0.5)
            speak(results)
        
        elif "youtube" in query:
            speak("Opening Youtube")
            webbrowser.open("youtube.com")
        
        elif "google" in query:
            speak("Opening google")
            webbrowser.open("google.com")

        elif "github" in query:
            speak("Opening github")
            webbrowser.open("github.com")



    
