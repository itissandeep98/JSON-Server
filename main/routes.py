from flask import render_template,jsonify
from main import app
import base64
import requests
import json

server_url = "https://jsonserver-f.herokuapp.com/"

def decode(content):
	content = base64.b64decode(content)
	content=content.decode("utf-8")
	content=content.replace("\t"," ")
	return content

def fetchrepo(username,repo):
	url = 'https://api.github.com/repos/'+username+'/'+repo+'/contents/db.json'
	req = requests.get(url)
	return req

def fetchUser(username):
	url = 'https://api.github.com/users/'+username
	req = requests.get(url)
	return req

def fetchSocialCircle(username):
	userList = {"Followers": [], "Following": []}
	url = "https://api.github.com/users/"+username+"/followers"
	req = requests.get(url)
	if req.status_code == requests.codes.ok:
		req = req.json()
		for i in req:
			userList["Followers"].append(server_url+i["login"])

	url = "https://api.github.com/users/"+username+"/following"
	req = requests.get(url)
	if req.status_code == requests.codes.ok:
		req = req.json()
		for i in req:
			userList["Following"].append(server_url+i["login"])
	
	return userList



def fetchAllRepo(username):
	repoList = {"Owned":[],"Starred":[]}
	url = "https://api.github.com/users/"+username+"/repos"
	req=requests.get(url)
	if req.status_code == requests.codes.ok:
		req=req.json()
		for i in req:
			repoList["Owned"].append(server_url+i["full_name"])
			
	url = "https://api.github.com/users/"+username+"/starred"
	req = requests.get(url)
	if req.status_code == requests.codes.ok:
		req = req.json()
		for i in req:
			repoList["Starred"].append(server_url+i["full_name"])
	return repoList


@app.route('/<username>/')
@app.route('/<username>')
def username(username):
	req=fetchUser(username)
	if req.status_code == requests.codes.ok:
		req=req.json()
		dic = {"Username": req["login"], "Repository List": fetchAllRepo(username),"Social Circle":fetchSocialCircle(username)}
		return dic
	else:
		return{"errmess":"User not found","status":404}

@app.route('/<username>/<repo>')
@app.route('/<username>/<repo>/')
def repo(username,repo):
	req=fetchrepo(username,repo)
	try:
		if req.status_code == requests.codes.ok:
			req = req.json()
			content = decode(req['content'])
			content=json.loads(content)			
		else:
			return{"errmess":'db.json file not found', "status":404}
	except Exception as e:
		return{"errmess":'Error in fetching the data', "status":404}
	return content

@app.route('/<username>/<repo>/<path:path>')
def path(username,repo,path):
	path=path.split("/")
	req=fetchrepo(username,repo)
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
		print(e)
		return{"errmess":'Error in fetching the data', "status":404}
	return jsonify(content)

@app.route('/')
def index():
	return render_template('index.html')
