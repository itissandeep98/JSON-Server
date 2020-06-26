# JSON Server
Its a simple Json server to fetch data without needing to setup any database and calling it via various api. 
Just store all data in a `db.json` file and upload it to any github repo.

## Setup
1. Clone this repo to you local machine
2. Install `pipenv`
3. Run `pipenv install` to install all the required dependencies
4. Run `python3 run.py` to start the flask server

## Usage
1. Create a db.json file in your repository which stores all your data in json format
2. Now you can fetch data from that file using this url `https://jsonserver-f.herokuapp.com/{username}/{reponame}`
#### Example
- repo: https://github.com/itissandeep98/ReactTest 
- link: https://jsonserver-f.herokuapp.com/itissandeep98/ReactTest/ \
  &ensp; &ensp; : https://jsonserver-f.herokuapp.com/itissandeep98/ReactTest/comments

#### PS: 
- There are other api also which does the same or even better work than this but they all come with a limitation of size or requirement of login into their site.
- Currently it only accepts `GET` requests.
- feel free to open any issue or Pull request
