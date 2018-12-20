import tweepy

counter = 0


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        try:
            print(status.extended_tweet['full_text'])
        except:
            print(status.text)


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
