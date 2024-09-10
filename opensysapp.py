import subprocess
from speaknmic import *

def open_application(app_name):
    try:
        subprocess.Popen([app_name], shell=True)
        speak(f"Opening {app_name}")
    except Exception as e:
        speak(f"Error opening {app_name}: {e}")