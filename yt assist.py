import speech_recognition as sr
import webbrowser
import requests
from bs4 import BeautifulSoup
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def is_normal_voice(recognizer, source):
    try:
        recognizer.adjust_for_ambient_noise(source)
        decibels = recognizer.energy_threshold
        print(f"Current ambient noise level: {decibels}")
        return decibels < 2000  # Adjust this threshold based on your environment
    except Exception as e:
        print(f"Error checking ambient noise level: {e}")
        return False

def open_youtube():
    youtube_url = "https://www.youtube.com/"
    webbrowser.open(youtube_url)
    speak("Opening YouTube")

def search_within_youtube(query):
    youtube_search_url = f"https://www.youtube.com/results?search_query={'+'.join(query.split())}"
    webbrowser.open(youtube_search_url)
    speak(f"Searching for {query} on YouTube")

def main():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something...")
        if is_normal_voice(recognizer, source):
            audio = recognizer.listen(source)

            try:
                print("Recognizing...")
                command = recognizer.recognize_google(audio).lower()
                print("You said:", command)

                if "open youtube" in command:
                    open_youtube()
                elif "go to youtube and search" in command:
                    query = command.replace("go to youtube and search", "").strip()
                    search_within_youtube(query)
                else:
                    speak("Command not recognized.")

            except sr.UnknownValueError:
                speak("Speech Recognition could not understand audio")
            except sr.RequestError as e:
                speak(f"Could not request results from Google Speech Recognition service; {e}")
            except Exception as e:
                speak(f"Error: {e}")
        else:
            print("Ambient noise level too high. Not recognizing.")

if __name__ == "__main__":
    main()
