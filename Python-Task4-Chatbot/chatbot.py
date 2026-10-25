print("--- OIBSIP Task 4 - Simple Chatbot ---")
print("Chatbot: Hello! I am your assistant. Type 'bye' to exit.")

while True:
    user = input("You: ").lower()
    if "hello" in user or "hi" in user:
        print("Chatbot: Hello Rakshitha! How can I help you?")
    elif "how are you" in user:
        print("Chatbot: I am great! Thanks for asking!")
    elif "your name" in user:
        print("Chatbot: I am OIBSIP Chatbot made by Rakshitha!")
    elif "help" in user:
        print("Chatbot: I can chat with you! Try asking me anything.")
    elif "bye" in user:
        print("Chatbot: Bye Rakshitha! Have a great day!")
        break
    else:
        print("Chatbot: Sorry, I didn't understand. Can you say again?")
