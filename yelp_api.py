#!/usr/bin/env python3
import os
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


def search_businesses(address):
	auth = Oauth1Authenticator(
   		consumer_key=os.environ['CONSUMER_KEY'],
    	consumer_secret=os.environ['CONSUMER_SECRET'],
    	token=os.environ["TOKEN"],
    	token_secret=os.environ["TOKEN_SECRET"]
	)	

	client = Client(auth)
	params = {
    	'term': 'food',
    	'lang': 'en', 
    	'limit': 3
	}

	response = client.search(address, **params)
	
	businesses = []
	
	
	
	for business in response.businesses:
		businesses.append(business.name)
		businesses.append(business.display_phone)
		businesses.append(business.image_url)


	return businesses


#for business in businesses:)
#print(businesses)
