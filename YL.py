import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import os

YL= pyttsx3.init()
voice=YL.getProperty('voices')
YL.setProperty('voice',voice[1].id)

def speak(audio):
    print('Y.L.:' + audio)
    YL.say(audio)
    YL.runAndWait()


def time():
    Time=datetime.datetime.now().strftime("%I:%M:%p")
    speak(Time)

def welcome():
    hour=datetime.datetime.now().hour
    if hour >=6 and hour <12:
        speak("Good Morning sir")
    elif hour >=12 and hour <18:
        speak("Good Afternoon sir")
    elif hour >=18 and hour <21:
        speak("Good Evening")
    speak('How can you I help you')

def command():
    c=sr.Recognizer()
    with sr.Microphone() as source:
            c.pause_threshold=2
            audio=c.listen(source)
    try:
        query=c.recognize_google(audio,language='en')
        print("Roberto CasLuan:" + query)
    except sr.UnknownValueError:
        print("Please repeat or typing the command")
        query=str(input('Your order is:  '))
    return query

if __name__ =="__main__":
    welcome()
    while True:
        query=command().lower()
        if"google" in query:
             speak("What should I search boss? ")
             search=command().lower()
             url=f"https://www.google.com/search?q={search}"
             wb.get().open(url)
             speak(f'Here is your {search} on google')
        if"youtube" in query:
             speak("What should I search boss? ")
             search=command().lower()
             url=f"https://www.youtube.com/search?q={search}"
             wb.get().open(url)
             speak(f'Here is your {search} on youtube')
        elif "open video" in query:
             meme=r"D:\NHU Y\meme.webm"
             os.startfile(meme)
        elif "time" in query:
             time()
        elif"quit"in query:
             speak("YL is quiting sir, Goobye boss")
             quit()