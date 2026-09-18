import random
print("="  * 45)
print("      PYTHON SMART CHATBOT")
print("=" *  45)
print("Bot:  Hello! I'm your Python chatbot.")
print("Bot: You can chat with me or type 'help'.")
print("Bot: Type 'bye' to exit.")
print("=" * 45)

while True:
    user = input("\nYou: ").lower().strip()
    if user in ["hello","hi","hey"]:
        responses = ["Hello! How can I help you?",
                     "Hey there!Nice to meet you!",
                     "Hi! What would you like to talk about?"
                     ]
        print("Bot:",random.choice(responses))
    elif user == "how are you?":
        print("Bot: I'm doing great ! Thanks  for asking!")
    elif user in ["what is your name?", "your name"]:
                  print('Bot: My name is PythonBot')
    elif user == "what is python?":
        print("Bot: Python is a beginner-friendly programming language")
    elif user == "help":
        print("\nBot: Here are some things you can ask me:")
        print("   .hello")
        print("   .how are you?")
        print("   .what is your name?")
        print("   .what is python?")
        print("   .Thank You!")
        print(" .Bye!")
    elif user in ["thanks","thank you"]:
                  print("Bot: You're Welcome!")
    elif user in ["bye","exit", "quit"]:
        print("Bot: Goodbye!")
        print("Bot: Keep learning Python!")
        exit()
    else:
        print("Bot: Hmm... I don't understand yet.")
        print("Bot: Type 'help' to see what I can answer.")
print("="* 45)
print("      CHAT ENDED!")
print("=" * 45)
  
    
    
