import pyttsx3      
import datetime
import speech_recognition as sr
from sqlalchemy import engine_from_config
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def text_to_speach(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        text_to_speach("good morning dear")
    elif hour>=12 and hour<18:
        text_to_speach('good afternoon dear')
    else:
        text_to_speach('good evening dear')        
    text_to_speach("Hi i am Akash Srivastava . Please tell me how may i help you")    

def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening.........')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('recogninzing......')
        query = r.recognize_google(audio, language='en-in')
        print("user said : ", query)

    except Exception as e:
        print(e)
        print("say that again......")
        return "None"

    return query
