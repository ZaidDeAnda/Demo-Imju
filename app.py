# ==============================================================
# Author: Zaid De Anda
# Twitter: @ndaZaid
#
# ABOUT COPYING OR USING PARTIAL INFORMATION:
# This script has been originally created by Rodolfo Ferro.
# Any explicit usage of this script or its contents is granted
# according to the license provided and its conditions.
# ==============================================================

# -*- coding: utf-8 -*-

import streamlit as st
import tweepy
import json
import logging
from config import create_api

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = create_api()

statuses=[]

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        if len(statuses) < 10:
            statuses.append(status)
        else:
            statuses.pop(0)
            statuses.append(status)
    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_error disconnects the stream
            return False

        # returning non-False reconnects the stream, with backoff.

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(track=['Guanajuato'])

st.header("Demo de implementación chikita")
st.write(statuses)