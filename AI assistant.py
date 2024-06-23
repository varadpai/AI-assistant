import os  # helps to interact with operating system, like opening files etc
import pyttsx3  # helps to convert text into speech
import datetime
import speech_recognition as sr  # Enables the program to understand and convert speech into text.
import wikipedia
import webbrowser
import smtplib

engine = pyttsx3.init('sapi5')  # This line initializes a text-to-speech engine using the SAPI5
# (Speech API version 5) technology. SAPI5 is a standard speech API developed by Microsoft for speech synthesis.
voices = engine.getProperty('voices')  # engine.getProperty('voices'): Retrieves a list of available voices that the
# text-to-speech engine (engine) can use. Each voice has a unique ID and other properties like language and gender.
print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning")
    elif 12 <= hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good evening")

    speak("Hello this is Jarvis, how may i help you?")


# In summary, takeCommand() is a function that listens to the user via a microphone, attempts to recognize what was
# said using Google's speech recognition, handles any errors that may occur during recognition, and returns the
# recognized text. This is a fundamental part of building voice-controlled applications or assistants where user
# input needs to be understood and processed.


def takeCommand():
    r = sr.Recognizer()  # Initializes a recognizer object from the speech_recognition library.
    # This object is used to recognize speech from audio input.
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        # noinspection PyBroadException
        try:
            print("Recognising...")
            query = r.recognize_google(audio, language='en-in')  # Uses Google's speech recognition service (
            # recognize_google) to convert the captured audio (audio) into text. It specifies the language as English
            # (India) using the language='en-in' parameter.
            print(f"user said:{query}\n")
        except Exception as e:
            print("Say that again pls")
            return "None"
        return query


# This block of code essentially creates a voice-controlled virtual assistant (similar to Jarvis) that can perform
# actions like searching Wikipedia, opening websites, telling the time, and launching applications based on voice
# commands provided by the user. It uses various libraries (pyttsx3, speech_recognition, wikipedia, webbrowser,
# os) to handle speech recognition, text-to-speech conversion, web browsing, and application launching functionalities.
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:  # if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            code_path = "C:\\Users\\Varad\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)
