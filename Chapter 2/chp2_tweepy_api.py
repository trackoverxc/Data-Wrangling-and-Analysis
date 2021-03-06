""" Simple tweepy stream listener for twitter API. """
from __future__ import print_function
import tweepy
import csv

try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser

class PythonListener(tweepy.StreamListener):
    """ Very simple tweepy stream listener. """
	#csvFile = open('result.csv','a')
	#csvWriter = csv.writer(csvFile)
    def on_status(self, tweet):
        print(tweet.text, tweet.author.screen_name)
        f = open('sample.csv','a')
        writer = csv.writer(f)
        writer.writerow([tweet.text])
        f.close()

    def on_error(self, msg):
        print('Error: %s', msg)

    def on_timeout(self):
        print('tweepy timeout. waiting before next poll')
        sleep(30)


def get_config():
    """ Return my config object. """
    conf = ConfigParser()
    conf.read('config/prod.cfg')
    return conf

config = get_config()
auth = tweepy.OAuthHandler(config.get('twitter', 'consumer_key'),
                           config.get('twitter', 'consumer_secret'))

auth.set_access_token(config.get('twitter', 'access_token'),
                      config.get('twitter', 'access_token_secret'))


my_listener = PythonListener()
my_stream = tweepy.Stream(auth = auth, listener=my_listener)

my_stream.filter(track=['#python', 'python'])
