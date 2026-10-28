import datetime
import webbrowser

import pyttsx3
import speech_recognition as sr


def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("\nListening... Please speak.")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)

        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()

    except sr.WaitTimeoutError:
        speak("I did not hear anything. Please try again.")
    except sr.UnknownValueError:
        speak("Sorry, I could not understand that.")
    except sr.RequestError:
        speak("Speech recognition service is unavailable.")
    except OSError:
        speak("Microphone not found. Please check your microphone.")

    return ""


def run_assistant():
    speak("Hello! Welcome to your Python voice assistant.")
    speak("Say help to hear the available commands.")

    while True:
        command = listen()

        if not command:
            continue

        if "hello" in command or "hi" in command:
            speak("Hello! How can I help you?")

        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak("The current time is " + current_time)

        elif "date" in command:
            current_date = datetime.datetime.now().strftime("%d %B %Y")
            speak("Today's date is " + current_date)

        elif "open google" in command:
            speak("Opening Google.")
            webbrowser.open("https://www.google.com")

        elif "open youtube" in command:
            speak("Opening YouTube.")
            webbrowser.open("https://www.youtube.com")

        elif command.startswith("search for "):
            query = command.replace("search for ", "", 1).strip()

            if query:
                speak("Searching Google for " + query)
                webbrowser.open(
                    "https://www.google.com/search?q="
                    + query.replace(" ", "+")
                )
            else:
                speak("Please say what you want to search for.")

        elif "help" in command:
            speak(
                "You can say hello, tell me the time, "
                "tell me the date, open Google, open YouTube, "
                "search for something, or stop."
            )

        elif "stop" in command or "exit" in command or "goodbye" in command:
            speak("Goodbye! Have a nice day.")
            break

        else:
            speak("Sorry, I do not know that command. Say help for options.")


if __name__ == "__main__":
    engine = pyttsx3.init()
    engine.setProperty("rate", 160)
    run_assistant()
