## Twitter-Sentiment-Analysis

In this assignment, I have

* Accessed the twitter Application Programming Interface (API) using python
* Estimated the public's perception (the sentiment) of a particular term or phrase
* Analyzed the relationship between location and mood based on a sample of twitter data

#### Problem 1: Getting the Twitter Data (twitterstream_py3.py)
Here I have accessed the Twitter data through the Twitter API. I have followed the following steps:

1. Create a twitter account if you do not already have one.
2. Go to https://dev.twitter.com/apps and log in with your twitter credentials.
3. Click "Create New App"
4. Fill out the form and agree to the terms. Put in a dummy website if you don't have one you want to use.
5. At this point you will be prompted to attach a mobile phone number to your account if you have not previously done so. Follow the instructions at the link provided.
6. On the next page, click the "Keys and Access Tokens" tab along the top, then scroll all the way down until you see the section "Your Access Token"
7. Click the button "Create My Access Token".
8. Now copy four values into the file twitterstream_py3.py. These values are your "Consumer Key (API Key)", your "Consumer Secret (API Secret)", your "Access token" and your "Access token secret". All four should now be visible on the "Keys and Access Tokens" page. 

The .py file is run through the following command on the terminal:
$ python twitterstream_py3.py

#### Problem 2: Deriving the sentiment of each tweet (tweet_sentiment.py)
For this part, I have computed the sentiment of each tweet based on the sentiment scores of the terms in the tweet. 
The sentiment of a tweet is equivalent to the sum of the sentiment scores for each term in the tweet.

The file AFINN-111.txt contains a list of pre-computed sentiment scores. Each line in the file contains a word or phrase followed by a sentiment score. Each word or phrase that is found in a tweet but not found in AFINN-111.txt is given a sentiment score of 0. 
See the file AFINN-README.txt for more information.

The script prints to stdout the sentiment of each tweet in the file, one numeric sentiment score per line. The first score corresponds to the first tweet, the second score should correspond to the second tweet, and so on. 

The .py file is run through the following command on the terminal:
$ python tweet_sentiment.py AFINN-111.txt output.txt

#### Problem 3: Deriving the sentiment of new terms in each tweet (term_sentiment.py)
In this part I have created a script that computes the sentiment for the terms that do not appear in the file AFINN-111.txt.

The script prints output to stdout. Each line of output contains a term, followed by a space, followed by the sentiment. That is, each line is in the format <term:string> <sentiment:float>

The .py file is run through the following command on the terminal:
$ python term_sentiment.py AFINN-111.txt output.txt

#### Problem 4: Computing term frequency (frequency.py)
The script frequency.py computes the term frequency histogram of the livestream data harvested from Problem 1.

The frequency of a term is calculated as [# of occurrences of the term in all tweets]/[# of occurrences of all terms in all tweets]

The .py file is run through the following command on the terminal:
$ python frequency.py output.txt

#### Problem 5: Which State is happiest? (happiest_state.py)
The script happiest_state.py returns the name of the happiest state as a string and takes a file of tweets as input. 

I have assigned a location to a tweet by usinf the coordinates field (a part of the place object, if it exists), to geocode the tweet. This method gives the most reliable location information, but unfortunately this field is not always available and you must figure out some way of translating the coordinates into a state.

The .py file is run through the following command on the terminal:
$ python happiest_state.py AFINN-111.txt output.txt

#### Problem 6: Top ten hash tags (top_ten.py)
The script top_ten.py computes the ten most frequently occurring hashtags from the data gathered in Problem 1.

The .py file is run through the following command on the terminal:
$ python python top_ten.py output.txt





