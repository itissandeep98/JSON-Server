# 1. Table of Contents

- [1. Table of Contents](#1-table-of-contents)
  - [1.1. Description](#11-description)
  - [1.2. Setup](#12-setup)
  - [1.3. Usage](#13-usage)
    - [1.3.1. Example](#131-example)
  - [1.4. PS](#14-ps)

## 1.1. Description

Its a simple Json server to fetch data without needing to setup any database and calling it via various API.
Just store all data in a `db.json` file and upload it to any github repo.

## 1.2. Setup

1. Clone this repo to your local machine
2. Install `pipenv`
3. Run `pipenv install` to install all the required dependencies
4. Run `python3 run.py` to start the flask server

## 1.3. Usage

1. Create a db.json file in your repository which stores all your data in json format
2. Now you can fetch data from that file using this url `https://jsonserver-f.herokuapp.com/{username}/{reponame}`

### 1.3.1. Example

- repo: <https://github.com/itissandeep98/ReactTest>
- link: <https://jsonserver-f.herokuapp.com/itissandeep98/ReactTest/> \
  &ensp; &ensp; : <https://jsonserver-f.herokuapp.com/itissandeep98/ReactTest/comments>

## 1.4. PS

- There are other api also which does the same or even better work than this but they all come with a limitation of size or requirement of login into their site.
- Currently it only accepts `GET` requests.
- feel free to open any issue or Pull request
