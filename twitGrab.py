from TwitterAPI import TwitterAPI
from gensim.models import Word2Vec
import sys

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
    out = []
    tweets = getTweets(sys.argv[1], api)
    for tweet in tweets:
        out.append(tweet.split())

    # Load model in
    model = Word2Vec.load("word2vec.model")
    
    for word in tweet:
        print(model.wv.most_similar(positive=word))


if __name__ == "__main__":
    main()
