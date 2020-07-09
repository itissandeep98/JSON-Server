from flask import render_template,jsonify,session
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
				"repository List": fetchAllRepo(username), 
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
	if(username+repo not in session):
		req = fetch('repos/'+username+'/'+repo+'/contents/'+dbfile)
	try:
		if username+repo in session or req.status_code == requests.codes.ok:
			if (username+repo in session):
				content = session[username+repo]
			else:
				req = req.json()
				content = decode(req['content'])
				content = json.loads(content)
				session[username+repo] = content
		else:
			return{"errmess":dbfile+' file not found', "status":404}
	except Exception as e:
		return req.json()

	return jsonify(content)

@app.route('/<username>/<repo>/<path:path>')
def path(username,repo,path):
	path=path.split("/")
	if(username+repo not in session):
		req = fetch('repos/'+username+'/'+repo+'/contents/'+dbfile)
	try:
		if username+repo in session or req.status_code == requests.codes.ok:
			if (username+repo in session):
				content=session[username]
			else:
				req = req.json()
				content = decode(req['content'])
				content=json.loads(content)
				session[username+repo] = content

			if(path[0]!=""):
				for i in path:
					if(i.isnumeric()):
						i=int(i)
					content=content[i]
			
		else:
			return{"errmess":dbfile+' file not found', "status":404}
	except Exception as e:
		return req.json()

	return jsonify(content)

@app.route('/')
def index():
	return render_template('index.html')
