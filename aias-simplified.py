import speech_recognition as sr
import webbrowser
import pyttsx3
import subprocess
import wikipedia

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', [v for v in voices if "female" in v.name.lower()][0].id)
    engine.say(text)
    engine.runAndWait()

def open_application(app_name):
    try:
        subprocess.Popen([app_name], shell=True)
        speak(f"Opening {app_name}")
    except Exception as e:
        speak(f"Error opening {app_name}: {e}")

def search_on_google(query):
    webbrowser.open(f"https://www.google.com/search?q={query}")
    speak(f"Search Results for '{query}'")

def open_website(url, name):
    webbrowser.open(url)
    speak(f"Opening {name}...")

def tell_about_topic(topic):
    try:
        content = wikipedia.summary(topic, sentences=2)
        print(content)
        speak(content)
    except (wikipedia.DisambiguationError, wikipedia.PageError):
        print(f"Sorry, I couldn't find information about {topic} on Wikipedia.")
        speak(f"Sorry, I couldn't find information about {topic} on Wikipedia.")

def main():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)

        if "open notepad" in command:
            open_application("notepad.exe")
        elif "open calculator" in command:
            open_application("calc.exe")
        elif "open youtube" in command:
            open_website("https://www.youtube.com/", "YouTube")
        elif "open gmail" in command:
            open_website("https://mail.google.com/mail/u/0/#inbox", "Gmail")
        elif "open chatbot" in command:
            open_website("https://chat.openai.com/", "Chat G P T")
        elif "open" in command:
            query = command.replace("open", "").strip()
            search_on_google(query)

        elif any(keyword in command for keyword in ["tell about", "about", "say about", "what is", "explain"]):
            topic = command.split(maxsplit=1)[-1]
            tell_about_topic(topic)

    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
