from flask import render_template, flash, redirect
from app import app
from forms import LoginForm
import requests
from requests_oauthlib import OAuth1
import json
from twkey import *
from words import *

@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
def index():
	form = LoginForm()
	posts = []
	if(form.twitter.data):
		url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
		twitter_auth = OAuth1(TW_APIKEY, TW_APISEC, TW_ACCTOK, TW_ACCSEC)
		twitter_params = {'screen_name': form.twitter.data, 'count':'100'}
		r = requests.get(url, params = twitter_params, auth=twitter_auth)
		if r.status_code == requests.codes.ok:
			data = json.loads(r.text)
			for tweets in data:
				posts.append(tweets['text'])
		else:
			form.twitter.data = ""
		mood = 0;
		for post in posts:
			words = post.split()
			for word in words:
				if word.lower() in positive:
					mood+=1
				elif word.lower() in negative:
					mood-=1
		print mood
	return render_template("index.html",
		form = form,
		posts = posts)

