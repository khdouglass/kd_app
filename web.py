#importing flask
from flask import Flask, render_template, request
import yelp_api
import os
import weather
#creating variable named app
app = Flask(__name__)


#creates page
@app.route("/")
def index():
	address = request.values.get('address')
	businesses = None
	#will only pass through function if there is an address
	if address:
		businesses = yelp_api.search_businesses(address)
	return render_template('index.html', businesses=businesses)

def index():
	address = request.values.get('address')
	forecast = None
	#will only pass through function if there is an address
	if address:
		forecast = weather.get_weather(address)
	return render_template('index.html', forecast=forecast)


#necessary to get application to run 
if __name__ == "__main__":
    app.run()
