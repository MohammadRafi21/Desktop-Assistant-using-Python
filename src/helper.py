import speech_recognition as sr
import google.generativeai as genai
import os
from gtts import gTTS

GOOGLE_API_KEY = "AIzaSyCQcaSKVyq6AlDIiZQcQNqb2x5I2jqE9eg"
os.environ['GOOGLE_API_KEY'] = GOOGLE_API_KEY

def voice_input(): # like the takecommand()
    """
    Docstring for takeCommand
    this function will recognize voice and return text
    """ 
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening..........")
        # r.pause_threshold = 1
        audio = r.listen(source) # this is using google api converting voice to text

        try:
            print("Recognizing...........")
            query = r.recognize_google(audio)
            print(f"user said: {query}\n")
            return query
        except sr.UnknownValueError:
            print("Sorry, unable to understand the audio")
        except sr.RequestError as e:
            print("Could not request results form Google speech Recognition service; {0}".format(e))
        # except Exception as e:
        #     print("Say that again please.......")
        #     return "None"
        # return query

def text_to_speech(text):
    # creating a gTTS object
    tts = gTTS(text=text, lang='en') # Language can be changed

    # Save the audio as an MP3 file
    tts.save("speech.mp3")



def llm_model_object(user_text):

    genai.configure(api_key=GOOGLE_API_KEY)

    model = genai.GenerativeModel('gemini-pro')

    response = model.generate_content(user_text)

    result=response.text

    return result

