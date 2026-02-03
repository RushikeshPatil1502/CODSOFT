print("🤖: Hello! welcome")

while True:
    user_input = input("👤: ").lower()

    if "hello" in user_input or "hi" in user_input:
        print("🤖: 👋 Hey there! How can I help you?")

    elif "how are you" in user_input:
        print("🤖: I'm doing great 👍, thanks for asking!")

    elif "your name" in user_input:
        print("🤖: Hey my Name is Rulby, I'm a rule-based chatbot 🤖!")

    elif "bye" in user_input:
        print("🤖: Goodbye! Have a nice day 👋")
        break

    else:
        print("🤖: I'm sorry! I don't understand what you are saying")
