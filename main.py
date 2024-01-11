from flask import Flask, render_template, request
import random
import pytest
from papybot.parser import Parser
from google_api.geocoding import Geocoding
from papybot.wikirequest import WikiRequest
from papybot.request_nok_sentence import request_nok_sentence
from papybot.request_ok_sentence import request_ok_sentence
import json


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
		if result["status"] == "OK":
			wikirequest = WikiRequest(result["location"]["lat"], result["location"]["lng"])
			pageid = wikirequest.get_pageid()
			summary = wikirequest.get_summary(pageid)
			#construit la réponse dans le cas OK
			# : STATUS : OK, Phrase de réponse random, LAT, LNG, PHRASE WIKI

			sentence = random.choice(request_ok_sentence)
			
			parameters = {
				"status" : result["status"],
				"lat" : result["location"]["lat"],
				"lng" : result["location"]["lng"] ,
				"sentence" : sentence,
				"wiki_sentence" : summary				
				}
			jsonStr = json.dumps(parameters)
			#print(jsonStr)
			#print(type(jsonStr))

		#	print(parameters)

			return jsonStr		
		else:

			sentence = random.choice(request_nok_sentence)
			parameters = {
				"status" : result["status"],
				"sentence" : sentence
			}
		
			jsonStr = json.dumps(parameters)
			return jsonStr
			#construit la réponse dans le cas NOK
			# STATUS : NOK et la phrase de réponse

		#return jsonfiy du dictionnaire

		#lat =  WikiRequest
		#lng = WikiRequest(lng)
		#get_pageid = WikiRequest(lat,lng)

		
		
#		print(keywords)
		return('',204)
	return (result)
if __name__ == "__main__":
	app.run(debug=True)
