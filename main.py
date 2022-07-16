from unicodedata import name
from chatterbot import ChatBot


# naming the ChatBot calculator
# using mathematical evaluation logic
# the calculator AI will not learn with the user input

Bot = ChatBot(name="Calculator",
               read_only = true,
               logic_adapters = ["chatterbot.logic.MathematicalEvaluation"],
               storage_adapters = "chatterbot.storage.SQLStorageAdapter")

print("Hello, I am a calculator Vishal. How may I help you?")
while (True):
    # take the input from the user
    user_input = input("me: ")

        # check if the user has typed quit to exit the prgram   
    if user_input.lower() == 'quit':
        print("Exiting")
        break

    # otherwise, evaluate the user input
    # print invalid input if the AI is unable to comprehend the input
    try:
        response = Bot.get_response(user_input)
        print("Calculator:", response)
    except:
        print("Calculator: Please enter valid input")