import requests
import base64

server_url = "https://jsonserver-f.herokuapp.com/"


def decode(content):
	content = base64.b64decode(content)
	content = content.decode("utf-8")
	content = content.replace("\t", " ")
	return content


def fetchrepo(username, repo):
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
	repoList = {"Owned": [], "Starred": []}
	url = "https://api.github.com/users/"+username+"/repos"
	req = requests.get(url)
	if req.status_code == requests.codes.ok:
		req = req.json()
		for i in req:
			repoList["Owned"].append(server_url+i["full_name"])

	url = "https://api.github.com/users/"+username+"/starred"
	req = requests.get(url)
	if req.status_code == requests.codes.ok:
		req = req.json()
		for i in req:
			repoList["Starred"].append(server_url+i["full_name"])
	return repoList
