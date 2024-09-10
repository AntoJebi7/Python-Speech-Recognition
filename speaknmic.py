import pyttsx3

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