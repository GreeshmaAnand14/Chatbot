
# STEP 6 - CHATBOT THAT REMEMBERS YOUR NAME

FILE_NAME = "chat_history.txt"
USER_FILE = "user_data.txt"


# Load or save user's name
try:
    with open(USER_FILE, "r", encoding="utf-8") as file:
        name = file.read().strip()

except FileNotFoundError:
    name = ""


# Ask for name if it is not saved
if not name:
    print("Chatbot: Hello! What is your name?")
    name = input("You: ").strip()

    if not name:
        name = "Friend"

    with open(USER_FILE, "w", encoding="utf-8") as file:
        file.write(name)


# Load previous conversations
try:
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        chat_history = file.readlines()

except FileNotFoundError:
    chat_history = []


# Chatbot responses
responses = {
    "hello": "Hello! How can I help you?",
    "hi": "Hi! Nice to meet you.",
    "how are you": "I am doing great!",
    "what is python": "Python is a programming language.",
    "who are you": "I am your personal chatbot."
}


# Function to generate responses
def get_response(message, name):

    message = message.lower()

    if "what is my name" in message:
        return "Your name is " + name + "."

    if "who am i" in message:
        return "You are " + name + "."

    for question in responses:
        if question in message:
            return responses[question]

    return "Sorry, I don't understand that."


# Function to save conversation
def save_message(message):

    with open(FILE_NAME, "a", encoding="utf-8") as file:
        file.write(message + "\n")


# Main chatbot program
print("\nWelcome back,", name + "!")
print("I remember your name.")
print("Type 'history' to see previous conversations.")
print("Type 'bye' to exit.")

while True:

    user_message = input("\nYou: ").strip()

    if user_message.lower() == "bye":
        print("Chatbot: Goodbye,", name + "!")
        break

    if user_message.lower() == "history":

        if len(chat_history) == 0:
            print("Chatbot: No previous conversations found.")

        else:
            print("\n--- CHAT HISTORY ---")
            print("".join(chat_history))

        continue

    # Generate response
    reply = get_response(user_message, name)

    # Store conversation
    chat_history.append("You: " + user_message + "\n")
    chat_history.append("Chatbot: " + reply + "\n")

    # Save conversation permanently
    save_message("You: " + user_message)
    save_message("Chatbot: " + reply)

    print("Chatbot:", reply)
