from ChatBot import ChatBot

#Main class where the bot will be run from.

cb = ChatBot()
cb.extractQuotes('quotes.txt') #we establish the quotes in the object

print("Calm Bot: Hello, my name is Calm Bot and I'm here to help you!")

exitWords = ['bye','quit','exit','see ya','good bye']

while(True):
    userInput = input()
    if userInput.lower() in exitWords:
        print("It was really nice talking to you!")
    else:
        if cb.helloMessage(userInput) != None:
            print("Calm Bot: " + cb.helloMessage(userInput))
        else:
            print("Calm Bot: " + cb.botResponse(userInput))


