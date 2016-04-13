# -*- coding: utf-8 -*-

import sys
import tweepy
import os
import xml.etree.cElementTree as ET

consumer_key = 'XXXXXXX'
consumer_secret = 'XXXXXXX'
access_token = 'XXXXXXX'
access_secret = 'XXXXXXX'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)


api = tweepy.API(auth)

#gets the last twits que veuria l'usuari al home
##display homepage tweets of authenticated user
for i in range(0, 5):
    print(" ")
print("...........---------/////////TL\\\\\\\\-------............")
print(" ")

root = ET.Element("root")
llistatuits = ET.SubElement(root, "llistatuits")

public_tweets = api.home_timeline(count=90)
for tweet in reversed(public_tweets):
    print("::::::::::::::::")
    hora= tweet.created_at.strftime('%H')
    #horari d'estiu
    hora= int(hora) + 2
    emisor= tweet.user.name + " - @" + tweet.user.screen_name
    print(emisor  + " -" + str(hora) + ":" + tweet.created_at.strftime('%M:%S'))
    #continguttuit=tweet.text.encode('latin-1', 'ignore').decode('utf-8', 'ignore')
    continguttuit=tweet.text.encode('latin-1', 'ignore').decode('utf-8', 'ignore')
    print (continguttuit)
    nretuits=str(tweet.retweet_count)
    print (nretuits)
    horatuit= str(hora) + ":" + tweet.created_at.strftime('%M:%S')
    if 'media' in tweet.entities:
        for image in  tweet.entities['media']:
            imatgetuit= image['media_url']
            ET.SubElement(llistatuits, "tuit", de=emisor, retuits=nretuits, hora=horatuit, imatge=imatgetuit).text = str(continguttuit)
    else:
        ET.SubElement(llistatuits, "tuit", de=emisor, retuits=nretuits, hora=horatuit).text = str(continguttuit)


tree = ET.ElementTree(root)
tree.write("dadestw.xml")

print(" ")

#OPCIÓ QUE OBRE AUTOMÀTICAMENT UNA FINESTRA DEL NAVEGADOR PER VISUALITZAR ELS TWEETS
#import webbrowser
#webbrowser.open_new('index.html')
