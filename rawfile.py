"""
Speech Recognition and Voice Assistant Documentation
Author: Anto Jebikshan  -LinkedIn
Date: January 13, 2024
Time: 12:00 pm
Description:
This Python program serves as a Speech Recognition and Voice Assistant application. It allows users to interact with their computer using voice commands, performing various tasks such as opening applications, searching the web, and more.

Requirements:
- Python 3.x
- SpeechRecognition library
- pyttsx3 library
- Other dependencies as needed

Installation:
1. Install required libraries:
2. just run the code :)
3. don't forget to add some credits :)
"""

import speech_recognition as sr
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime
import pyttsx3
import subprocess
from twilio.rest import Client
import wikipedia
import sys
import opener as whp
import requests
import openai
'''
from twilio.rest import Client

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='',
  to=''
)
'''

'''
account_sid = ""
auth_token = ""
twilio_phone_number = ""
your_phone_number = ""
def send_sms(message):
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=message,
        from_=twilio_phone_number,
        to=your_phone_number
    )

    print(f"SMS sent with SID: {message.sid}")
'''


def speak(text):
    engine = pyttsx3.init()
    # Get all available voices
    voices = engine.getProperty('voices')
    # Select a female voice
    for voice in voices:
        if "female" in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break
    engine.say(text)
    engine.runAndWait()
def check_for_restricted_words(text):
    restricted_words = ["stupid", "idiot", "looser","password", "secret", "authentication", "token", "confidential", "private"]  # Add your restricted words here
    for word in restricted_words:
        if word.lower() in text.lower():
            return True
    return False
def tell_about_topic(topic):
    try:
        content = wikipedia.summary(topic, sentences=2)  # Adjust the number of sentences as needed
        print(content)
        speak(content)
    except wikipedia.DisambiguationError as e:
        print(f"There are multiple results for {topic}. Please specify your request.")
        speak(f"There are multiple results for {topic}. Please specify your request.")
    except wikipedia.PageError as e:
        print(f"Sorry, I couldn't find information about {topic} on Wikipedia.")
        speak(f"Sorry, I couldn't find information about {topic} on Wikipedia.")

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning, I'm a virtual assistant, How can I help you today?")
    elif hour>=12 and hour<18:
        speak("Good Afternoon,I'm a virtual assistant, How can I help you today?")
    else:
        speak("Good Evening,I'm a virtual assistant, How can I help you today?")
def open_application(app_name):
    try:
        subprocess.Popen([app_name], shell=True)
        speak(f"Opening {app_name}")
    except Exception as e:
        speak(f"Error opening {app_name}: {e}")


def search_on_google(query):
    driver = webdriver.Chrome()
    driver.get(f"https://www.google.com/search?q={query}")
    print(f"Searching for '{query}' on Google...")
    speak(f"Search Results for '{query}' ")
    time.sleep(5)
    #print("listening")
    try:
        print("Waiting for 5 seconds...")
        speak("Closing in 5 seconds...")
        time.sleep(5)
        driver.quit()
        print("Window closed.")
        speak("Window closed.")
    except Exception as e:
        print(f"Error closing the window: {e}")
        speak(f"Error closing the window: {e}")


def open_ghub():
    ghb_url = "https://github.com/"
    webbrowser.open(ghb_url)
    speak("Opening Github...")
def open_linkd():
    lkd_url = "https://www.linkedin.com/feed/?"
    webbrowser.open(lkd_url)
    speak("Opening Linkedin...")
def open_flp():
    flp_url = "https://www.flipkart.com/"
    webbrowser.open(flp_url)
    speak("Opening Flipkart...")
def open_amz():
    amz_url = "https://www.amazon.in/"
    webbrowser.open(amz_url)
    speak("Opening Amazon...")
def open_youtube():
    youtube_url = "https://www.youtube.com/"
    webbrowser.open(youtube_url)
    speak("Opening YouTube...")
def open_map():
    map_url = "https://www.google.com/maps/@8.6647745,77.5733936,15z?entry=ttu"
    webbrowser.open(map_url)
    speak("Opening Google Maps...")
def open_gmail():
    gmail_url = "https://mail.google.com/mail/u/0/#inbox"
    webbrowser.open(gmail_url)
    speak("Opening gmail...")
def open_gpt():
    gpt_url = "https://chat.openai.com/"
    webbrowser.open(gpt_url)
    speak("Opening Chat G P T...")
def main():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("for searching on google use - 'Search on google' while speaking' eg: search about Mobiles on google ")
        print("for opening the application use - 'open while speaking' eg: open calculator ")
        print("For Getting information about anything , use 'Tell About' while speaking ")
        #time.sleep(1)
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)

        # Check for restricted words
        if check_for_restricted_words(command):
            print("The input contained restricted and not allowed words. Action restricted or Blocked")
            print("The service is no longer available.")
            # Send SMS notification
            #sms_message = f"Security Alert: Restricted word found - '{command}'"
            #send_sms(sms_message)
            sys.exit()
            # Split the recognized text into words
        words = command.split()


        if "open notepad" in command:
            open_application("notepad.exe")
        if "open calculator" in command:
            open_application("calc.exe")
        if "open youtube" in command:
            open_youtube()
        if "open gmail" in command:
            open_gmail()
        if "open chatbot" in command:
            open_gpt()
        if "open google maps" in command:
            open_map()
        if "open linkedin" in command:
            open_linkd()
        if "open amazon" in command:
            open_amz()
        if "open flipkart" in command:
            open_flp()
        if "open github" in command:
            open_ghub()
        if "open whatsapp" in command:
            whp.open_whatsapp()

        if "tell about" in command:
            topic = command.replace("tell about", "").strip()
            tell_about_topic(topic)
        elif "about" in command:
            topic = command.replace("about", "").strip()
            tell_about_topic(topic)
        elif "say about" in command:
            topic = command.replace("say about", "").strip()
            tell_about_topic(topic)
        elif "what is" in command:
            topic = command.replace("what is", "").strip()
            tell_about_topic(topic)
        elif "explain" in command:
            topic = command.replace("explain", "").strip()
            tell_about_topic(topic)
        # Add more applications as needed

    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    except Exception as e:
        print(f"Error: {e}")



    try:
        print("Processing...")
        command = recognizer.recognize_google(audio).lower()
        print("Results for:", command)
        print("Documented and Programmed By Anto Jebikshan")


        if "open" in command:
            query = command.replace("open", "").strip()
            search_on_google(query)
        if "reopen" in command:
            query = command.replace("reopen", "").strip()
            search_on_google(query)
        if "go to google and search" in command:
            query = command.replace("go to google and search", "").strip()
            search_on_google(query)

        elif "close" in command:
            print("Closing the last opened browser window...")

        if "go to google search" in command:
            query = command.replace("go to google search", "").strip()
            search_on_google(query)
        elif "google" in command:
            query = command.replace("google", "").strip()
            search_on_google(query)
        elif "search" in command:
            query = command.replace("search", "").strip()
            search_on_google(query)
        elif "browser" or "on" in command:
            query = command.replace("browser", "").strip()
            search_on_google(query)

    except sr.UnknownValueError:
        print("Could not Understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google ; {e}")

    #speak("Documented and Programmed By Anto Jebik shan")

if __name__ == "__main__":
    wishMe()
    main()

