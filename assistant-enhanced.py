import speech_recognition as sr
import webbrowser
import subprocess
import pyttsx3
import datetime
import shutil
import os

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for voice in voices:
        if "female" in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break
    engine.say(text)
    engine.runAndWait()

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning, I'm a virtual assistant, How can I help you today?")
    elif 12 <= hour < 18:
        speak("Good Afternoon, I'm a virtual assistant, How can I help you today?")
    else:
        speak("Good Evening, I'm a virtual assistant, How can I help you today?")


def find_executable_path(app_name):
    try:
        result = subprocess.run(["where", app_name], capture_output=True, text=True, check=True)
        paths = result.stdout.strip().split('\n')
        if paths:
            return paths[0]
        else:
            return None
    except subprocess.CalledProcessError as e:
        print(f"Error finding executable path for {app_name}: {e}")
        return None



def open_application(app_name):
    app_path = find_executable_path(app_name)

    if app_path is not None:
        try:
            subprocess.Popen([app_path], shell=True)
            speak(f"Opening {app_name}")
        except Exception as e:
            speak(f"Error opening {app_name}: {e}")
    else:
        speak(f"Application {app_name} not found.")

def search_on_google(query):
    webbrowser.open(f"https://www.google.com/search?q={query}")
    speak(f"Search Results for '{query}'")

def main():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say or Search about something...")
        print("for searching on google use - 'Search on google' while speaking' eg: search about Mobiles on google ")
        print("for opening the application use - 'open while speaking' eg: open calculator ")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)

        if "open" in command:
            app_name = command.replace("open", "").strip()
            open_application(app_name)
        elif "search on google" in command:
            query = command.replace("search on google", "").strip()
            search_on_google(query)

    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    except Exception as e:
        print(f"Error: {e}")

    speak("Program execution completed.")

if __name__ == "__main__":
    wish_me()
    main()
