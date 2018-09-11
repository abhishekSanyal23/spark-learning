# -*- coding: utf-8 -*-
"""
Spyder Editor

This will generate Twitter data from twwtpy api
"""

#Setting up the imports
import tweepy
from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener
import socket
import json


# Consumer keys
consumer_key = 'TIr4VkXBwb4YUxT6AJWSuosyp'
consumer_secret = 'Yo9QP6H75tXkyAaDzc8u28gnBjhjQWOQ9DPTDJH8CfnXwYi2wL'
access_token = '160185140-3hYX803hrCXcntMBV2MKrllDAYhkMuQ7st1jPRxl'
access_secret = '49iiS1qVyVyeJFwBCxJ8mYL1XTHSdcFeLBdiZeGjjrtEX'

# Setting up Tweet Listener

class TweetListener(StreamListener):
    
    def __init__(self, csocket):
        self.client_socket = csocket
        
    def on_data(self, data):
        try:
            msg = json.loads(data)
            print(msg['text'].encode('utf-8'))
            self.client_socket.send(msg['text'].encode('utf-8'))
        except BaseException as e:
            print ('ERROR ', e)
        finally:
            return True
        
    def on_error(self, status):
        print (status)
        return True
    
# Set up send Data
def sendData(c_socket):
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    
    twitter_stream = Stream(auth, TweetListener(c_socket))
    twitter_stream.filter(track = ['India'])
    
    
# Main Function
if __name__ == '__main__':
    s = socket.socket()
    host = '127.0.0.1'
    port = 9999
    s.bind((host, port))
    
    print('Listening on port 9999')
    
    s.listen(5)
    c, addr = s.accept()
    
    sendData(c)

