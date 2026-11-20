
# STEP 7 - CHATBOT WITH DATE, TIME AND GREETINGS

import datetime
from zoneinfo import ZoneInfo

FILE_NAME = "chat_history.txt"
USER_FILE = "user_data.txt"


# Load user's name
try:
    with open(USER_FILE, "r", encoding="utf-8") as file:
        name = file.read().strip()

except FileNotFoundError:
    name = ""


# Ask for name if not available
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

    "what is artificial intelligence": "Artificial Intelligence allows machines to perform tasks that normally require human intelligence.",

    "what is machine learning": "Machine Learning is a branch of AI where computers learn from data.",

    "who created python":"Python was created by Guido van Rossum.",

    "what is html":  "HTML stands for HyperText Markup Language.",

    "what is cpu":  "CPU stands for Central Processing Unit. It is the brain of a computer.",

    "what is internet": "The Internet is a global network that connects computers and devices.",

    "what is programming":"Programming is the process of writing instructions for computers.",

    "what is database": "A database is an organized collection of information.",

    "what is robotics": "Robotics is a field that involves designing, building and programming robots.",

    "what is iot": "IoT stands for Internet of Things. It connects physical devices to the internet."

}


# Function for date, time and greetings
def get_time_response(message):
    now = datetime.datetime.now(ZoneInfo("Asia/Kolkata"))

    if "date" in message or "today" in message:
        return "Today's date is " + now.strftime("%d %B %Y") + "."

    elif "day" in message:
      "Today is " + now.strftime("%A") + "."
    
    elif "time" in message:
        return "The current time is " + now.strftime("%I:%M %p") + "."

    elif "good morning" in message or "good afternoon" in message or "good evening" in message:

        hour = now.hour

        if hour < 12:
            return "Good morning, " + name + "!"

        elif hour < 17:
            return "Good afternoon, " + name + "!"

        else:
            return "Good evening, " + name + "!"

    return None

# Function to perform calculations
def calculate(message):

    parts = message.split()

    if parts[0] != "calculate":
        return None

    try:
        num1 = float(parts[1])
        operator = parts[2]
        num2 = float(parts[3])

        if len(parts) != 4:
            return "Please enter two numbers and one operator."

        if operator == "+":
            result = num1 + num2

        elif operator == "-":
            result = num1 - num2

        elif operator == "*":
            result = num1 * num2

        elif operator == "/":
            if num2 == 0:
                return "Cannot divide by zero."

            result = num1 / num2

        else:
            return "Invalid mathematical operator."

        # Display whole numbers without decimal points
        if result.is_integer():
            result = int(result)

        return "The answer is " + str(result) + "."

    except (ValueError, IndexError):
        return "Please enter a valid calculation."


# Function to generate chatbot response
def get_response(message):

    message = message.lower()

    if "what is my name" in message:
        return "Your name is " + name + "."

    if "who am i" in message:
        return "You are " + name + "."

    # Check date, time and greetings
    time_response = get_time_response(message)

    if time_response is not None:
        return time_response
    math_response = calculate(message)

    if math_response is not None:
        return math_response
    # Check normal responses
    for question in responses:

        if question in message:
            return responses[question]

    return "Sorry, I don't understand that."


# Function to save conversations
def save_message(message):

    with open(FILE_NAME, "a", encoding="utf-8") as file:
        file.write(message + "\n")


# Display greeting based on current time
hour = datetime.datetime.now(ZoneInfo("Asia/Kolkata")).hour

if hour < 12:
    greeting = "Good morning"
elif hour < 17:
    greeting = "Good afternoon"
else:
    greeting = "Good evening"


print("\n" + greeting + ", " + name + "!")
print("I can tell you the date and time.")
print("Type 'history' to see previous conversations.")
print("Type 'bye' to exit.")


# Main chatbot loop
while True:

    user_message = input("\nYou: ").strip()

    if user_message.lower() == "bye":
        print("Chatbot: Goodbye, " + name + "!")
        break

    if user_message.lower() == "history":

        if len(chat_history) == 0:
            print("Chatbot: No previous conversations found.")

        else:
            print("\n--- CHAT HISTORY ---")
            print("".join(chat_history))

        continue

    # Generate response
    reply = get_response(user_message)

    # Save conversation
    chat_history.append("You: " + user_message + "\n")
    chat_history.append("Chatbot: " + reply + "\n")

    save_message("You: " + user_message)
    save_message("Chatbot: " + reply)

    print("Chatbot:", reply)
