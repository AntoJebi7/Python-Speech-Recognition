import openai
import pyttsx3

openai.api_key = "your-api-key"  # Replace with your GPT-3 API key

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def answer_question(question):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"I have a question: {question}",
        max_tokens=150
    )

    answer = response.choices[0].text.strip()
    speak(f"You asked: {question}. Here's my response: {answer}")

# Example usage
user_question = input("Ask me something: ")
answer_question(user_question)
