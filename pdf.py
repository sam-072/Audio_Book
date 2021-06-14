import pyttsx3
import PyPDF2
import speech_recognition as sr
import os
import smtplib
import time
import subprocess
import requests
import json
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty("rate",140)


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,phrase_time_limit = 5)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")

    except Exception as e:
        print(e)
        speak("pardon me , please say it again")
        return "None"

    return query

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")
    elif hour>=12 and hour<18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("welcome back sir !")
    speak("I am alexa. please tell me how may i help you!")


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


if __name__ == "__main__":
    wishMe()
    book =open('How to make anyone fall in love with you - Leil Lowndes.pdf','rb')
    pdfReader=PyPDF2.PdfFileReader(book)
    pages=pdfReader.numPages

    while True:

        query = takeCommand().lower()

        if 'good bye' in query or 'ok bye' in query or 'stop' in query:
            speak("your personal assistant alexa is shutting down , good bye sir")
            speak("have a nice day ahead sir")
            break

        elif 'middle' in query:
            speak('which page you want to read')
            page_no=int(takeCommand())
            page=pdfReader.getPage(page_no-1)  #strarting from index 0
            text=page.extractText()
            speak(text)


        elif 'number of pages' or 'total pages' in query:
            speak("the total number of pages in this pdf is")
            speak(pages)
        
        




