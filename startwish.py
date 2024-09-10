import datetime
from speaknmic import *
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning, I'm a virtual assistant, How can I help you today?")
    elif hour>=12 and hour<18:
        speak("Good Afternoon,I'm a virtual assistant, How can I help you today?")
    else:
        speak("Good Evening,I'm a virtual assistant, How can I help you today?")
