import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser as wb
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
newVoiceRate = 180
engine.setProperty('rate', newVoiceRate)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")


def takecommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='hi=in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)

        print("Say that again please....")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak("searching Wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif 'search in chrome' in query:
            speak("What should I search ? ")
            chromepath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
            search = takecommand().lower()

        elif 'open youtube' in query:
            wb.open("youtube.com")

        elif 'open google' in query:
            wb.open("google.com")

        elif 'open stackoverflow' in query:
            wb.open("stackoverflow.com")

        elif 'romantic song' in query:
            wb.open("youtube.com/watch?v=tfchHFd3CvU&list=PLBfVFpmZYypAed-1USo5KwFrqbmp1FtPL&index=1")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, thr time is {strTime}")
            print(strTime)
        elif 'offline' in query:
            quit()

takecommand()
