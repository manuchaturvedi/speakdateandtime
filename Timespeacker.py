import pyttsx3
import datetime

engine=pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    Time=datetime.datetime.now().strftime("%H:%M:%S")
    speak("and the current time is")
    speak(Time)


def date_():
    year =datetime.datetime.now().year
    month=datetime.datetime.now().month
    date=datetime.datetime.now().day
    speak("the current date is ")
    speak(date)
    speak(month)
    speak(year)
    time_()


def wishme():
    speak("welcome back mach!")
    date_()    
    
    hour=datetime.datetime.now().hour

    if hour>=6 and hour<=12:
        speak("good morning sir!")
    elif hour>=12 and hour<=18:
        speak("good afternoon sir!")
    elif hour>=18 and hour<=24:
        speak("good evening sir!")
    else:
        speak("good night sir")

wishme()    