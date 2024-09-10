from librs import *
from speaknmic import *
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

