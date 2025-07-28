import datetime

def get_response(user_input):
    user_input = user_input.lower()
    
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you?"
    elif "how are you" in user_input:
        return "I'm just a bunch of code, but I'm doing great! 😊"
    elif "ip address" in user_input:
        return "I dont have an IP address like a regular device"
    elif "sing a song" in user_input:
        return "Sorry,I dont have a voice assistance to speak or sing"
    elif "your name" in user_input:
        return "I'm ChatPy, your Python chatbot!"
    elif "time" in user_input:
        now = datetime.datetime.now()
        return f"The current time is {now.strftime('%H:%M:%S')}"
    elif "date" in user_input:
        today = datetime.date.today()
        return f"Today's date is {today.strftime('%B %d, %Y')}"
    elif "bye" in user_input or "exit" in user_input:
        return "bye"
    else:
        return "Sorry, I didn't understand that."

def main():
    print("🤖 ChatPy: Hello! I am your chatbot. Type 'bye' to exit.")
    while True:
        user = input("You: ")
        response = get_response(user)
        if response == "bye":
            print("🤖 ChatPy: Goodbye! Have a great day!")
            break
        else:
            print("🤖 ChatPy:", response)

if __name__ == "__main__":
    main()
