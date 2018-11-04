from TwitterAPI import TwitterAPI
from gensim.models import Word2Vec
import gensim.downloader as api
import sys
import re
import string
from nltk.tokenize import TweetTokenizer
import preprocessor
tknzr = TweetTokenizer(strip_handles=True)
from pycontractions import Contractions

# Load your favorite semantic vector model in gensim keyedvectors format from disk
cont = Contractions(api_key="glove-twitter-100")

def getTweets(query, api):
    r = api.request('search/tweets', {'q':query})
    tweetList = []
    for item in r:
        if(item['lang'] == 'en'):
            tweetList.append(item['text'])
    return tweetList

def main():
    # Interface with OPSUS sentiment analysis API
    api = TwitterAPI('7ldroPca5V9h2GczFb2ySRuqS',
                    'Di98ZN3xmRcoeL3St1Xe6fEo6expkyNZLezdwn2ON8sUCK2t6T',
                    '1049876480447123457-cEA1uhUauGFjA1oPGxpUB2tCJGAaen',
                    'xsGol4ZwM6FRLxiM2ucp80brUDENKdn3r3pf0h8yhEO5t')
    # Get all of the tweets mentioning the brand of interest
    tweets = getTweets(sys.argv[1], api)

    preprocessedTweets = {preprocessor.clean(tweet.encode('utf-8').lower()) for tweet in tweets}
    preprocessedTweets = cont.expand_texts(preprocessedTweets)
    print('processed')

    model = Word2Vec.load("word2vec.model")
    for tweet in preprocessedTweets:
        print(tweet)

        tweet = re.sub(r'\b\w{1,3}\b', '', tweet)

        print(tweet.translate(string.punctuation))
        words = tweet.split()
        for word in words:
            print(word)
            print(model.wv.most_similar(positive=word))


if __name__ == "__main__":
    main()
