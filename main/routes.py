from flask import render_template,jsonify
from main import app
from main.worker import *
import json

@app.route('/<username>')
@app.route('/<username>/')
def username(username):
	req = fetch('users/'+username)
	if req.status_code == requests.codes.ok:
		req=req.json()
		dic = {"Username": req["login"], "Repository List": fetchAllRepo(
			username), "Social Circle": fetchSocialCircle(username)}
		return dic
	else:
		return req.json()

@app.route('/<username>/<repo>')
@app.route('/<username>/<repo>/')
def repo(username,repo):
	req = fetch('repos/'+username+'/'+repo+'/contents/db.json')
	try:
		if req.status_code == requests.codes.ok:
			req = req.json()
			content = decode(req['content'])
			content=json.loads(content)			
		else:
			return{"errmess":'db.json file not found', "status":404}
	except Exception as e:
		return{"errmess":'Error in fetching the data', "status":404}

	return jsonify(content)

@app.route('/<username>/<repo>/<path:path>')
def path(username,repo,path):
	path=path.split("/")
	req = fetch('repos/'+username+'/'+repo+'/contents/db.json')
	try:
		if req.status_code == requests.codes.ok:
			req = req.json()
			content = decode(req['content'])
			content=json.loads(content)
			if(path[0]!=""):
				for i in path:
					if(i.isnumeric()):
						i=int(i)
					content=content[i]
			
		else:
			return{"errmess":'db.json file not found', "status":404}
	except Exception as e:
		return{"errmess":'Error in fetching the data', "status":404}

	return jsonify(content)

@app.route('/')
def index():
	return render_template('index.html')
