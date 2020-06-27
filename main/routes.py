from flask import render_template,jsonify
from main import app
from main.worker import *
import json

@app.route('/<username>')
@app.route('/<username>/')
def username(username):
	req=fetchUser(username)
	if req.status_code == requests.codes.ok:
		req=req.json()
		dic = {"Username": req["login"], "Repository List": fetchAllRepo(
			username), "Social Circle": fetchSocialCircle(username)}
		return dic
	else:
		return{"errmess":"User not found","status":404}

@app.route('/<username>/<repo>')
@app.route('/<username>/<repo>/')
def repo(username,repo):
	req = fetchrepo(username, repo)
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
	req = fetchrepo(username, repo)
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
