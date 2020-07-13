import requests
import base64

server_url = "https://jsonserver-f.herokuapp.com/"
# server_url = "http://127.0.0.1:5000/"
api_url ='https://api.github.com/'
content_url = 'https://raw.githubusercontent.com/'
dbfile = "db.json"

def decode(content):
	content = base64.b64decode(content)
	content = content.decode("utf-8")
	content = content.replace("\t", " ")
	return content


def fetch(path):
	url = api_url+path
	req = requests.get(url,auth=("itissandeep98",""))
	return req

def fetchfile(username,repo):
	url=content_url+username+"/"+repo+"/master/"+dbfile
	req=requests.get(url)
	return req

def fetchfollowers(username):
	followers=[]
	req = fetch("users/"+username+"/followers")
	if req.status_code == requests.codes.ok:
		req = req.json()
		for i in req:
			followers.append(server_url+i["login"])
	return followers

def fetchfollowing(username):
	following=[]
	req = fetch("users/"+username+"/following")
	if req.status_code == requests.codes.ok:
		req = req.json()
		for i in req:
			following.append(server_url+i["login"])
	return following

def fetchstarred(username):
	starred=[]
	req = fetch("users/"+username+"/starred")
	if req.status_code == requests.codes.ok:
		req = req.json()
		for i in req:
			starred.append(server_url+i["full_name"])
	return starred

def fetchAllRepo(username):
	repoList = {"owned": [], "starred": server_url+username+"/starred"}
	req = fetch("users/"+username+"/repos")
	if req.status_code == requests.codes.ok:
		req = req.json()
		for i in req:
			repoList["owned"].append(server_url+i["full_name"])

	return repoList
