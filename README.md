# Speech Recognition and Voice Assistant

## Overview
This Python program serves as a Speech Recognition and Voice Assistant application. It allows users to interact with their computer using voice commands, performing tasks such as opening applications, searching the web, and retrieving information from Wikipedia.


## Date
January 13, 2024

## Description
The application recognizes speech commands and performs actions based on the recognized input. It can open applications, search the web, provide Wikipedia summaries, and more. The program is designed for project purposes and includes features like voice feedback and command execution.

## Requirements
- Python 3.x
- `SpeechRecognition` library
- `pyttsx3` library
- `selenium` library
- `wikipedia` library
- `requests` library
- `openai` library (optional, for future integration)
- `twilio` library (optional, for SMS notifications)

## Installation
1. Install the required libraries using pip:
   ```bash
   pip install SpeechRecognition pyttsx3 selenium wikipedia-api requests openai twilio


## Usage

### Voice Commands:
- Use commands such as:
  - `"open notepad"` to launch the Notepad application.
  - `"search about [topic] on Google"` to perform a Google search for the specified topic.
  - `"tell about [topic]"` to get information from Wikipedia on the given topic.
- For example:
  - Say `"open calculator"` to launch the Calculator application.
  - Say `"tell about Python"` to receive a summary about Python from Wikipedia.

### Features:
- **Speech Recognition**: Converts spoken commands into text for further processing.
- **Application Control**: Opens specified applications such as Notepad, Calculator, and more.
- **Web Search**: Executes Google searches based on voice commands and provides results.
- **Information Retrieval**: Fetches summaries from Wikipedia on various topics.
- **Voice Feedback**: Uses text-to-speech (TTS) to communicate responses and provide feedback.

## Notes
- **Restricted Words**: The application detects and blocks commands containing restricted or sensitive words to prevent misuse.
- **SMS Notifications**: An optional feature for sending security alerts via Twilio. Currently commented out and not active in the project.

## Future Updates
The program will be updated with additional features and improvements, including:
- Enhanced integration with additional APIs for expanded functionality.
- Improved error handling and overall robustness.
- New features and functionalities based on user feedback and needs.

## Contributing
Contributions to enhance the application are encouraged. To contribute:
1. Fork the repository.
2. Create a feature branch.
3. Make your changes and test thoroughly.
4. Submit a pull request with a clear description of your changes.

## License
This project is for personal and educational use. If you use or modify the code, please provide appropriate credit.


