import pyttsx3
import datetime
import wikipedia
import webbrowser
import speech_recognition as sr
engine=pyttsx3.init("sapi5")
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def tell_about_topic(topic):
    try:
        content = wikipedia.summary(topic, sentences=2)  # Adjust the number of sentences as needed
        speak(content)
    except wikipedia.DisambiguationError as e:
        speak(f"There are multiple results for {topic}. Please specify your request.")
    except wikipedia.PageError as e:
        speak(f"Sorry, I couldn't find information about {topic} on Wikipedia.")
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("goodmorning everyone")
    elif hour>=12 and hour<18:
        speak("goodafternoon everyone")
    else:
        speak("goodevening everyone")
    speak(" i am Chitti how can i help you?")
def takecommand():
    command=input("say something:")
    if "hi" in command:
        #print("Greetings! How can I help you?")
        command=command.replace("hi","hello")
        return command
    if "mobiles" in command:
        #print("Greetings! How can I help you?")
        command=command.replace("about mobiles","mobiles")
        return command
    if "youtube" in command:
        link = 'https://www.youtube.com/'
        webbrowser.open(link)
    if "chatgpt" in command:
        link = 'https://www.youtube.com/'
        webbrowser.open(link)



if __name__ == "__main__":
    wishMe()
    while True:
        query=takecommand().lower()
        if  query:
            speak("searching the command")
            results=wikipedia.summary(query,sentences=2)
            speak("According to the command")
            print(results)
            speak(results)