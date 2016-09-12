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

#necessary to get application to run 
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
