import sys
import re
import json

def topHashtags(file):
    #This function returns the top 10 hastags
    
    #Empty dictionary to store the hastags and its frequency
    hashtagDict={}
    for line in file:

        #parsing every line in the file and converting it from json to a regular string
        result = json.loads(line)

        #Getting the "entities" part of the above string which contains hastags
        entitiesHash = result.get('entities','NA')
        
        if entitiesHash != 'NA':
            hashtags = entitiesHash.get('hashtags','NA')
            #print(hashtags, len(hashtags))
            
            if hashtags != 'NA':
                for i in range(0,len(hashtags)): #There can be mutliple hashtags. Thus, we loop over all of them
                    hashtag = hashtags[i].get('text')
                    hashtagDict[hashtag] = hashtagDict.get(hashtag,0) + 1 #Taking the count of the hastags
    
    #Sorting the hastag dictionary as per the frequency in descending order
    sortedHashtagDict =  sorted(hashtagDict.items(), key=lambda t: t[1], reverse = True)
    
    print("\nTop 10 hastags are:")
    for i in range(10):
        hashtag,freq = sortedHashtagDict[i]
        print(hashtag, "\t", freq)

def main():
    tweetFile = open(sys.argv[1])
    topHashtags(tweetFile)

if __name__ == '__main__':
    main()