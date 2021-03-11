from ChatBot import ChatBot
from ChatBot import install

#Main class where the bot will be run from.

install('nltk')
install('scikit-learn')

cb = ChatBot()
cb.extractQuotes('quotes.txt') #we establish the quotes in the object

print("Calm Bot: Hello, my name is Calm Bot and I'm here to help you!")

exitWords = ['bye','quit','exit','see ya','good bye'] #Exit the chat bot with common greetings

while(True):
    userInput = input()
    if userInput.lower() in exitWords:
        print("It was really nice talking to you!")
    else:
        if cb.helloMessage(userInput) != None:
            print("Calm Bot: " + cb.helloMessage(userInput))
        else:
            print("Calm Bot: " + cb.botResponse(userInput))
