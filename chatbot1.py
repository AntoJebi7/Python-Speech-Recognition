from googlesearch import search
# need paid google api key or open ai api key otherwise program will not run
#documented by Anto Jebikshan on 13.01.2024 ,Saturday
def search_google(query):
    try:
        # Perform a Google search and return the first result
        for result in search(query, num=1, stop=1, pause=2):
            return result
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Sorry, I couldn't fetch the information."

# Main loop for user interaction
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break

    if "google" in user_input.lower():
        query = user_input.replace("google", "").strip()
        response = search_google(query)
    else:
        response = "I'm not sure. You can try asking Google for more accurate information."

    print("Chatbot:", response)

