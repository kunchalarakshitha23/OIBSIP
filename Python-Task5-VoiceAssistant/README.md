# Voice Assistant – Python Task 5

## About
This project is a simple voice assistant developed using Python as part of the Oasis Infobyte Python Internship. It listens to voice commands, processes them, and responds using speech.

## Features
- Accepts voice input through a microphone.
- Responds to greetings such as "Hello".
- Tells the current time and date.
- Opens Google and YouTube using voice commands.
- Searches Google for a spoken query.
- Provides a help command to list supported commands.
- Exits when the user says "stop", "exit", or "goodbye".
- Converts text responses into speech.

## Technologies Used
- Python
- SpeechRecognition
- PyAudio
- pyttsx3
- datetime
- webbrowser

## Requirements
- Python 3.13 recommended for this setup
- A working microphone
- Internet connection for speech recognition
- Required Python libraries

## Installation
Install the required libraries using:

```bash
python -m pip install SpeechRecognition pyttsx3 pyaudio
```

## How to Run
1. Open the project folder in VS Code.
2. Open the terminal in the project folder.
3. Run the program:

```bash
python voice_assistant.py
```

4. Allow microphone access if prompted.
5. Speak a supported command and wait for the assistant's response.

## Example Commands
- Hello
- What is the time?
- Tell me the date
- Open Google
- Open YouTube
- Search for Python programming
- Help
- Stop

## Author
Kunchala Rakshitha

Oasis Infobyte Python Internship – Task 5
