
import json
import sys
import re

statesDict = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

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
    
    return finalScore
    
def getHappiestState(file, sent_scores):
    #This functions returns all the tweet text collected 
    
    #print("\nFinal score of each tweet (The first line represents the score of the first tweet and so on):")

    states = {}
    stateFreq = {}

    for line in file:
		
        #parsing every line in the file and converting it from json to a regular string
        result = json.loads(line) 
        
        #Getting the "text" part of the above string
        txt = result.get('text','NA')

        #Getting the "place" part of the above string
        place = result.get('place',None)

        if place!=None:
            
            #Gettingt he country code
            countryCode = place.get('country_code',None)

            #Getting the state abbreviation
            stateAbbreviation = place.get('full_name',None)[-2:]
            
            #Getting scores only for the US states
            if countryCode == 'US':

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
                finalScore = getScore(allWordsOfSentence, sent_scores)
                #getScore(txt, sent_scores)

                #Getting the full name of the state from the state dictionary defined above
                stateFullname = statesDict.get(stateAbbreviation,'NA')

                #Populating the states dictionary which has the state and corresponding final scores
                states[stateFullname] = finalScore + states.get(stateFullname,0)

                #Populating the stateFreq dictionary which has the state and corresponding state frequency
                stateFreq[stateFullname] = stateFreq.get(stateFullname,0) + 1

        # dummy value for taking sum of scores of tweets for every state divided by total tweets from that state
        maxScore = -99999

        #To store the happiest state
        happiestState = ''
        
        #Finding the happiest state
        for state in states.keys():
            #print(state)
            if(maxScore < states[state]/stateFreq[state]):
                maxScore = states[state]/stateFreq[state]
                happiestState = state
    
    #Printing the happiest state    
    print("\nHappiest State is", happiestState, "with a sentiment score of", maxScore, "\n")



def main():
    #The first argument from the console corresponds to the sentiment score file (AFINN-111.txt)
    sentimentFile = open(sys.argv[1])

    #The second argument from the console corresponds to the output file generated from the twitter API
    tweetFile = open(sys.argv[2])

    #Getting the sentiment score dictionary
    sentScores = getSentimentDictionary(sentimentFile)

    getHappiestState(tweetFile, sentScores)


if __name__ == '__main__':
    main()
