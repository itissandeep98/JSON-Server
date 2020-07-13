from flask import render_template,jsonify
from main import app
from main.worker import *
import json

@app.route('/<username>')
@app.route('/<username>/')
def username(username):
	req = fetch('users/'+username)
	# print(req.headers['X-RateLimit-Remaining'])
	if req.status_code == requests.codes.ok:
		req=req.json()
		info = {"username": req["login"], 
				"repositories": fetchAllRepo(username), 
				"social": {
					"followers": server_url+username+"/followers", 
					"following": server_url+username+"/following"
					}
				}
		return info
	else:
		return req.json()

@app.route('/<username>/followers')
def followers(username):
	return jsonify(fetchfollowers(username))


@app.route('/<username>/following')
def following(username):
	return jsonify(fetchfollowing(username))

@app.route('/<username>/starred')
def starred(username):
	return jsonify(fetchstarred(username))

@app.route('/<username>/<repo>')
@app.route('/<username>/<repo>/')
def repo(username,repo):
	req = fetchfile(username,repo)
	if req.status_code == requests.codes.ok:
		req = req.json()
		return req
	else:
		return {"errmess":dbfile+' file not found', "status":404}

@app.route('/<username>/<repo>/<path:path>')
def path(username,repo,path):
	path=path.split("/")
	if( "" in path):
		path.remove("")
	req = fetchfile(username,repo)
	if req.status_code == requests.codes.ok:
		req = req.json()
		try:
			if(path[0]!=""):
				for i in path:
					if(i.isnumeric()):
						i=int(i)
					req=req[i]
		except:
			return {"errmess": "not valid path", "status": 404}
		return req

			
	else:
		return {"errmess":dbfile+' file not found', "status":404}
	
	

@app.route('/')
def index():
	return render_template('index.html')
