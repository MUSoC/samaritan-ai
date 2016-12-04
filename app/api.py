from app import app
from flask import jsonify, request, render_template

import json
import time

auth_key = "TheDayTheWorldWentAway"

def json_formatter(code, message, data):
	resp = jsonify({
		'code': code,
		'message': message,
		'data': data
	})
	resp.status_code = code
	return resp

# Index
@app.route('/', methods=['GET'])
def homepage():
	return render_template('index.html')

# Main route
# Make a POST request to /api; Header field 'auth_key': 'TheDayTheWorldWentAway'
# curl -X POST -H "auth_key=TheDayTheWorldWentAway" -F "text=somerandomtext"" -F "confidence=0.8" <URL>
@app.route('/api', methods=['POST'])
@app.route('/api/', methods=['POST'])
def getintent():
	if request.headers.get('auth_key') == auth_key:
		data = request.get_json()
		try:
			text = data['text']
			# confidence = float(data['confidence'])
			return json_formatter(200, "It works!", {"text": text, "keywords_detected": text, "hypothesis": text, "confidence": 0.69})
		except:
			return json_formatter(400, "Bad request", {})
	else:
		return json_formatter(401, "Unauthorized", {})
