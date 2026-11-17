
# STEP 5 - CHATBOT WITH PERMANENT MEMORY

name = "Greeshma"

FILE_NAME = "chat_history.txt"

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


# Function to save messages
def save_message(message):

    with open(FILE_NAME, "a", encoding="utf-8") as file:
        file.write(message + "\n")


# Function to generate responses
def get_response(message):

    message = message.lower()

    for question in responses:
        if question in message:
            return responses[question]

    return "Sorry, I don't understand that."


# Main chatbot program
print("Welcome", name, "!")
print("I can remember our previous conversations.")
print("Type 'history' to see your chat history.")
print("Type 'bye' to exit.")

while True:

    user_message = input("\nYou: ")

    if user_message.lower() == "bye":
        print("Chatbot: Goodbye!")
        break

    # Display previous conversations
    if user_message.lower() == "history":

        if len(chat_history) == 0:
            print("Chatbot: No previous conversations found.")

        else:
            print("\n--- CHAT HISTORY ---")
            print("".join(chat_history))

        continue

    # Generate chatbot response
    reply = get_response(user_message)

    # Store messages in memory
    chat_history.append("You: " + user_message + "\n")
    chat_history.append("Chatbot: " + reply + "\n")

    # Save messages permanently
    save_message("You: " + user_message)
    save_message("Chatbot: " + reply)

    print("Chatbot:", reply)
