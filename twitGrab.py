import tweepy
import re
from string import punctuation
from nltk.tokenize import TweetTokenizer
import preprocessor
import contractions
tknzr = TweetTokenizer(strip_handles=True)


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        try:
            tweet = status.extended_tweet['full_text']
        except:
            tweet = status.text
        tweet = initialPreprocess(tweet)
        tweet = custom_preprocess(tweet)
        print(tweet)


def getTweets(query, api):
    r = api.request('search/tweets', {'q': query})
    tweetList = []
    for item in r:
        if(item['lang'] == 'en'):
            tweetList.append(item['text'])
    return tweetList


def initialPreprocess(tweet):
    return preprocessor.clean(tweet.encode('ascii', 'ignore').lower())


def strip_punctuation(tweet):
    return ''.join(c for c in tweet if c not in punctuation)


def strip_rt(tweet):
    return tweet.replace('rt  ', '')


def fix_contractions(tweet):
    return contractions.fix(tweet)


def duplicate_whitespace(tweet):
    return re.sub(' +', ' ', tweet)


def custom_preprocess(tweet):
    tweet = fix_contractions(tweet)
    tweet = strip_punctuation(tweet)
    tweet = strip_rt(tweet)
    tweet = duplicate_whitespace(tweet)
    return tweet


def main():

    auth = tweepy.OAuthHandler('7ldroPca5V9h2GczFb2ySRuqS',
                               'Di98ZN3xmRcoeL3St1Xe6fEo6expkyNZLezdwn2ON8sUCK2t6T'
                               )

    auth.set_access_token('1049876480447123457-cEA1uhUauGFjA1oPGxpUB2tCJGAaen',
                          'xsGol4ZwM6FRLxiM2ucp80brUDENKdn3r3pf0h8yhEO5t'
                          )

    api = tweepy.API(auth)

    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
    myStream.filter(languages=["en"], track=['pizza'])


if __name__ == "__main__":
    main()
