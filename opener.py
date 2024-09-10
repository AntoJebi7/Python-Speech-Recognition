import webbrowser
import pyttsx3
import subprocess


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
def open_whatsapp():
    try:
        subprocess.Popen(["start", "whatsapp://"], shell=True)
    except Exception as e:
        print(f"Error opening WhatsApp: {e}")

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