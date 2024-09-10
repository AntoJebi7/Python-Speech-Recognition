def check_for_restricted_words(text):
    restricted_words = ["stupid", "idiot", "looser","password", "secret", "authentication", "token", "confidential", "private"]  # Add your restricted words here
    for word in restricted_words:
        if word.lower() in text.lower():
            return True
    return False