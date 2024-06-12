# Voice Assistant

## Description

This project is a basic voice assistant designed for beginners in Python. It can perform simple tasks based on voice commands, such as responding to "Hello", telling the current time or date, and searching the web for information.

## Features

- Responds to greetings.
- Tells the current time.
- Provides today's date.
- Searches the web based on user queries.

## Requirements

- Python 3.x
- `speech_recognition` library
- `pyttsx3` library
- `datetime` library (included in Python standard library)
- `webbrowser` library (included in Python standard library)

## Installation

1. Make sure you have Python 3.x installed on your system.
2. Install the required libraries using pip:
   ```bash
   pip install SpeechRecognition pyttsx3
   ```

## Usage

1. Clone this repository or download the code files.
2. Run the `voice_assistant.py` file:
   ```bash
   python voice_assistant.py
   ```
3. The voice assistant will initialise and start listening for your commands.

## Functionality

- **Greeting Response**: The assistant will respond to "Hello" with a greeting.
- **Time Inquiry**: Ask "What is the time?" to get the current time.
- **Date Inquiry**: Ask "What is the date?" to get today's date.
- **Web Search**: Say "Search for" followed by your query to search the web.

## Example Commands

- "Hello"
- "What is the time?"
- "What is the date?"
- "Search for Python tutorials"

## Code Overview

### Initialisation

```python
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
```

### Getting Voice Commands

```python
def get_voice_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
            return None
```

### Handling Commands

```python
def handle_command(command):
    if "hello" in command:
        speak("Hello! How can I assist you today?")

    elif "time" in command:
        now = datetime.datetime.now()
        speak(f"The current time is {now.strftime('%H:%M')}")

    elif "date" in command:
        today = datetime.date.today()
        speak(f"Today's date is {today.strftime('%B %d, %Y')}")

    elif "search" in command:
        speak("What do you want to search for?")
        search_query = get_voice_command()
        if search_query:
            url = f"https://www.google.com/search?q={search_query}"
            webbrowser.open(url)
            speak(f"Here are the search results for {search_query}")

    else:
        speak("Sorry, I didn't understand that command.")
```

### Running the Assistant

```python
def run_voice_assistant():
    speak("Voice Assistant initialized. How can I help you?")
    while True:
        command = get_voice_command()
        if command:
            handle_command(command)

run_voice_assistant()
```

## Contact

If you have any questions, feedback, or collaboration requests, please feel free to reach out to me at [e.adewusi@alustudent.com](mailto:e.adewusi@alustudent.com).
