
# STEP 4 - CHATBOT WITH CONVERSATION MEMORY

name = "Greeshma"

# Store conversation messages
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
def get_response(message):

    message = message.lower()

    if message == "history":
        if len(chat_history) == 0:
            return "No conversation history yet."

        return "\n".join(chat_history)

    for question in responses:
        if question in message:
            return responses[question]

    return "Sorry, I don't understand that."


# Main chatbot program
print("Welcome", name, "!")
print("Type 'history' to see previous messages.")
print("Type 'bye' to exit.")

while True:

    user_message = input("\nYou: ")

    if user_message.lower() == "bye":
        print("Chatbot: Goodbye!")
        break

    # Store user message
    chat_history.append("You: " + user_message)

    # Generate chatbot response
    reply = get_response(user_message)

    # Store chatbot response
    chat_history.append("Chatbot: " + reply)

    print("Chatbot:", reply)
