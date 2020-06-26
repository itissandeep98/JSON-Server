from flask import render_template
from main import app
import pandas as pd
from flask_cors import cross_origin
import base64
import requests
import json

@app.route('/<username>/<repo>')
@app.route('/<username>/<repo>/')
@app.route('/<username>/<repo>/<path:path>')
def method_name(username,repo,path=""):
	path=path.split("/")
	url = 'https://api.github.com/repos/'+username+'/'+repo+'/contents/db.json'
	req = requests.get(url)
	try:
		if req.status_code == requests.codes.ok:
			req = req.json()
			content = base64.b64decode(req['content'])
			content=content.decode("utf-8")
			content=content.replace("\t"," ")
			content=json.loads(content)
			if(path[0]!=""):
				for i in path:
					if(type(content)==list):
						content=content[int(i)]
					else:
						content=content[i]
				content={path[-1]:content}
			
		else:
			return{"errmess":'Content was not found', "status":404}
	except Exception as e:
		return{"errmess":'Content was not found', "status":404}
		

	return content

@app.route('/')
def index():
	return render_template('index.html')