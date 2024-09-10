import wikipedia
from speaknmic import *
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
