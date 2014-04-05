from app import app
from flask import render_template, flash, redirect
from forms import LoginForm
from requests_oauthlib import OAuth1
from twkey import *
from alkey import *
from words import *
import json
import requests

@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
def index():
	form = LoginForm()
	posts = []
	mood = ""
	if(form.twitter.data):
		tw_url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
		twitter_auth = OAuth1(TW_APIKEY, TW_APISEC, TW_ACCTOK, TW_ACCSEC)
		twitter_params = {'screen_name': form.twitter.data, 'count':'100'}
		r = requests.get(tw_url, params = twitter_params, auth=twitter_auth)
		if r.status_code == requests.codes.ok:
			tw_data = json.loads(r.text)
			for tweets in tw_data:
				posts.append(tweets['text'])
			tweets = ' '.join(posts)
			al_url = 'http://access.alchemyapi.com/calls/text/TextGetTextSentiment'
			al_params = {'apikey':AL_KEY, 'text':tweets,'outputMode':'json'}
			al_r = requests.post(al_url, data=al_params)
			al_data = json.loads(al_r.text)
			mood = str(al_data['docSentiment']['score'])
		else:
			form.twitter.data = ""
	"""pos_level = 0.0;
	neg_level = 0.0;
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
		for post in posts:
			words = post.split()
			for word in words:
				if word.lower() in positive:
					pos_level+=1
				elif word.lower() in negative:
					neg_level+=1
	if pos_level + neg_level > 0:
		mood = pos_level/(pos_level+neg_level)
	else:
		mood = 0
	"""
	return render_template("index.html",
		form = form,
		mood = mood)

