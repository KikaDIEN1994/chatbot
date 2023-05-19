from flask import Flask, render_template, request
import pytest
from papybot.parser import Parser
from google_api.geocoding import Geocoding
from papybot.wikirequest import WikiRequest


app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route('/question', methods=['POST'])
def question():
	is_request_ok = False 
	if request.method=='POST':

		print(request.form.get('question'))
		parser = Parser(request.form.get('question'))
		keywords = parser.parse()
		print(keywords)
		geocode = Geocoding(keywords)
		result = geocode.geocode()


		#lat =  WikiRequest.
		#lng = WikiRequest(lng)
		#get_pageid = WikiRequest(lat,lng)

		
		
#		print(keywords)
		return('',204)
		return (result)
if __name__ == "__main__":
	app.run(debug=True)
