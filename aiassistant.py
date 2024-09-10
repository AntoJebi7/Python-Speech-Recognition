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
from librs import *

'''
from twilio.rest import Client

account_sid = ' '
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_=' ',
  to=' '
)
'''

'''
account_sid = " "
auth_token = " "
twilio_phone_number = " "
your_phone_number = " "
def send_sms(message):
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=message,
        from_=twilio_phone_number,
        to=your_phone_number
    )

    print(f"SMS sent with SID: {message.sid}")
'''

             

def main():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("GOOGLE SEARCH - 'Search on google' while speaking' eg: search about Mobiles on google ")
        print("TO OPEN - 'open while speaking' eg: open calculator ")
        print("WIKIPEDIA INFO -  use 'Tell About' while speaking ")
        time.sleep(0.1)
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
            op.open_youtube()
        if "open gmail" in command:
            op.open_gmail()
        if "open chatbot" in command:
            op.open_gpt()
        if "open google maps" in command:
            op.open_map()
        if "open linkedin" in command:
            op.open_linkd()
        if "open amazon" in command:
            op.open_amz()
        if "open flipkart" in command:
            op.open_flp()
        if "open github" in command:
            op.open_ghub()
        if "open whatsapp" in command:
            op.open_whatsapp()
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

    #speak("Documented and Programmed By Anto Jebikshan")

if __name__ == "__main__":
    wishMe()
    main()
