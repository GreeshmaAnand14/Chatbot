
print("================================")
print("        MY CHATBOT")
print("================================")

# Store chatbot responses in a dictionary
responses = {
    "how are you": "I am doing great! Thanks for asking.",
    "your name": "I am your personal chatbot.",
    "what can you do": "I can chat with you and answer basic questions.",
    "i am doing great": "That's wonderful! What are you working on?",
    "what is python": "Python is a popular programming language."
}
# Function to generate chatbot responses
def get_response(message, name):

    message = message.lower().strip()
    words = message.split()

    if "bye" in words:
        return "Goodbye " + name + "! Have a nice day."

    elif "hello" in words or "hi" in words:
        return "Hello! How are you?"

    else:
        # Search for a matching question in dictionary
        for question in responses:

            if question in message:
                return responses[question]

        return "Sorry, I don't understand that yet."


# Main program
name = input("What is your name? ")

print("Hello", name)
print("Start chatting with me!")
print("Type 'bye' to exit.")

while True:

    user_message = input("You: ")

    # Call the response function
    reply = get_response(user_message, name)

    print("Bot:", reply)

    if "bye" in user_message.lower().split():
        break
