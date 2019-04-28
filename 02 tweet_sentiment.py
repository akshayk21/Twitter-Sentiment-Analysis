import json
import sys
import re


def getSentimentDictionary(file):
   #To read the sentiment scores from AFINN-111 file into a dictionary
    sentimentScoreDict = {}
    
    #This for loop reads the terms and its corresponding sentiment score into a dictionary
    for line in file:
        term, score = line.split("\t")
        sentimentScoreDict[term] = int(score) #Storing term and score into a dictionary
    
    return sentimentScoreDict
    
def getScore(list,sentimentScores):
    
    #Through this function, each word (list) in a tweet is scored against the sentiment 
    #score dictionary
    
    #This will simply store the final sentiment score of all the words in a tweet
    finalScore = 0
    
    
    for word in list: 
        
        #Checking if a particular word is there in the disctionary, then adding 
        #its score to finalScore
        
        if word in sentimentScores.keys():
            word = word.lower()
            finalScore += sentimentScores[word]
    
    print(finalScore)
    
def getTweets(file, sent_scores):
    #This functions returns all the tweet text collected 
    
    print("\nFinal score of each tweet (The first line represents the score of the first tweet and so on):")

    for line in file:
		
        #parsing every line in the file and converting it from json to a regular string
        result = json.loads(line) 
        
        #Getting the "text" part of the above string
        txt = result.get('text','NA')

        #Removing mentions
        txt = re.sub(r'@[A-Za-z0-9_]+', '', txt)

        #Removing hyperlinks
        txt = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', 
                    '', txt, flags=re.MULTILINE)
        
        #Removing retweets
        txt = re.sub(r'RT :', '', txt)
        
        #This finds all the words (charaterized by the '\w' regex) and compiles them separately
        #This is required to get the sentiment score of each owrd in the txt string
        
        #If we only use txt as argument to getScore function, it will give the score of the entire
        #sentence and not the score of each word of the sentence.

        #Thus, allWordsOfSentence id a list containing all the words of a sentence
        allWordsOfSentence = re.compile('\w+').findall(txt)

        #print(allWords)
        #print(txt)
        getScore(allWordsOfSentence, sent_scores)
        #getScore(txt, sent_scores)

def main():
    #The first argument from the console corresponds to the sentiment score file (AFINN-111.txt)
    sentimentFile = open(sys.argv[1])

    #The second argument from the console corresponds to the output file generated from the twitter API
    tweetFile = open(sys.argv[2])

    #Getting the sentiment score dictionary
    sentScores = getSentimentDictionary(sentimentFile)

    getTweets(tweetFile, sentScores)


if __name__ == '__main__':
    main()