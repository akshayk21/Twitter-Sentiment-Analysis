import json
import sys
import re

    
def getFrequency(file):
    #This functions returns all the tweet text collected 

    count = 0

    #Empty dictionary to contain store all the word frequencies
    terms = {}
    
    print("\nTerm Frequency for each word")

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

        #This loop stores exh word from each line into a dictionary along with its respective frequency
        for word in allWordsOfSentence:
            word = word.lower()
            terms[word] = terms.get(word,0) + 1
            count = count + 1

    #This loop prints all the term frequncies whose values are greater than an assumed value of 0.01
    for word, freq in terms.items():
        if (freq/count > 0.01):
            print(word, "\t", freq/count)


def main():
    #The first argument from the console corresponds to the output file generated from the twitter API
    tweetFile = open(sys.argv[1])

    getFrequency(tweetFile)


if __name__ == '__main__':
    main()