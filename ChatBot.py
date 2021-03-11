#Libraries needed to install:
    # nltk, scikit-learn

#Import libraries
import random
import string
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
nltk.download('punkt', quiet = True)  #this package is required to tokenize sentences

#This the class of the chatbot which reads quotes from a file and places them into a list
#When the bot runs, it runs a similarity test between each quote in the list and the input of the user
#The quote that is most similar to the users' input is outputted so that quotes match the topic the user talks about

#Import quotes from file
class ChatBot():
    CV = CountVectorizer()
    quotes = [] #lines taken from file will be placed in quotes and used to talk to user
    def __init__(self):
        print("bot initialized")
        
    def extractQuotes(self, fileName):
        file = open("quotes.txt", 'r', encoding='utf-8')
        text = file.read()
        file.close()
        self.quotes = nltk.sent_tokenize(text)

    
    def helloMessage(self, userInput):
        userInput = userInput.lower() #make everything lowercase so bot can doesn't deal with cases

        #ChatBot hello messages
        botHellos = ['Hello','Good day', 'Hey!', 'Hi!', 'Nice to meet you!', 'Hello there!']
        #User possible hello messages
        userHellos = ['hello', "what's up", 'hey', 'hi', 'hello', 'howdy','sup','hey there']

        for word in userInput.split():
            if word in userHellos:
                return random.choice(botHellos)

    def sortIndexList(self, scoresList):
        length = len(scoresList)
        retList = list(range(0,length -1))

        for i in range(length - 1):
            for j in range(length -1):
                if scoresList[retList[i]] > scoresList[retList[j]]:
                    temp = retList[i]
                    retList[i] = retList[j]
                    retList[j] = temp
        return retList

    def botResponse(self, userInput):
        userInput = userInput.lower()   #convert text to lowercase
        self.quotes.append(userInput)   #add users' input to end of quotes list
        response = ' '                   #initialize the bots response
        countArray = self.CV.fit_transform(self.quotes)             ##these two lines form the similarity scores between
        similarityScores = cosine_similarity(countArray[-1], countArray)    ##each quote and the users input to output the most similar one
        similarityScoresList = similarityScores.flatten()   #similarityScores is not a 1 dimensional array, so we flatten it
        indexOfQuote = self.sortIndexList(similarityScoresList)  #this gives us the indices of the most similar to least similar quotes
        self.quotes.remove(userInput)
        print(len(similarityScoresList), " and ", len(indexOfQuote))
        if similarityScoresList[indexOfQuote[0]].any() != 0.00:
            return response + self.quotes[indexOfQuote[0]]
        else:
            return response + "I'm sorry, I didn't quite understand what you just typed."

p = ChatBot()
p.extractQuotes('quotes.txt')

print("Calm Bot: Hello, my name is Calm Bot and I'm here to help you!")
exitWords = ['bye','quit','exit','see ya','good bye']
