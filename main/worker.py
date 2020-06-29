import requests
import base64
import os

server_url = "https://jsonserver-f.herokuapp.com/"
api_url ='https://api.github.com/'

def decode(content):
	content = base64.b64decode(content)
	content = content.decode("utf-8")
	content = content.replace("\t", " ")
	return content


def fetch(path):
	url = api_url+path
	req = requests.get(url,auth=("itissandeep98",""))
	return req


def fetchSocialCircle(username):
	userList = {"Followers": [], "Following": []}
	req = fetch("users/"+username+"/followers")
	if req.status_code == requests.codes.ok:
		req = req.json()
		for i in req:
			userList["Followers"].append(server_url+i["login"])

	req = fetch("users/"+username+"/following")
	if req.status_code == requests.codes.ok:
		req = req.json()
		for i in req:
			userList["Following"].append(server_url+i["login"])

	return userList


def fetchAllRepo(username):
	repoList = {"Owned": [], "Starred": []}
	req = fetch("users/"+username+"/repos")
	if req.status_code == requests.codes.ok:
		req = req.json()
		for i in req:
			repoList["Owned"].append(server_url+i["full_name"])

	req = fetch("users/"+username+"/starred")
	if req.status_code == requests.codes.ok:
		req = req.json()
		for i in req:
			repoList["Starred"].append(server_url+i["full_name"])
	return repoList
