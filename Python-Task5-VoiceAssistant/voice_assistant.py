print("--- OIBSIP Task 5 - Voice Assistant (Demo) ---")
print("Voice Assistant: Hello Rakshitha! I am your voice assistant.")

while True:
    command = input("You (type command): ").lower()
    if "hello" in command:
        print("Assistant: Hello! How can I help?")
    elif "time" in command:
        import datetime
        print(f"Assistant: Current time is {datetime.datetime.now().strftime('%H:%M:%S')}")
    elif "date" in command:
        import datetime
        print(f"Assistant: Today is {datetime.datetime.now().strftime('%d-%m-%Y')}")
    elif "search" in command:
        print("Assistant: Opening Google search (demo)...")
    elif "bye" in command or "exit" in command:
        print("Assistant: Goodbye Rakshitha! Have a great day!")
        break
    else:
        print("Assistant: Sorry, command not recognized. Try 'time', 'date', 'hello', 'bye'")
