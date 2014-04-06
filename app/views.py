from app import app
from flask import render_template, flash, redirect
from forms import LoginForm
from requests_oauthlib import OAuth1
from twkey import *
from alkey import *
from words import *
import json
import pyen
import requests

def get_mood(_mood_val):
	if _mood_val < 0:
		return "angry"
	elif _mood_val < 0.11:
		return "sad"
	elif _mood_val < 0.22:
		return "relaxing"
	elif _mood_val < 0.35:
		return "happy"
	else:
		return "excited"

@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
def index():
	form = LoginForm()
	tracks = []
	posts = []
	mood = ""
	first_song = ""
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
			mood_val = al_data['docSentiment']['score']
			mood = get_mood(float(mood_val))
			print mood_val
			en = pyen.Pyen("KDS5VIPB1DQPBQKR6")

			ec_url = 'http://developer.echonest.com/api/v4/playlist/static'
			ec_params = {'api_key': 'KDS5VIPB1DQPBQKR6','mood':mood,'type': 'artist-description','results': '20','bucket': ['id:rdio-US', 'tracks']}
			ec_r = requests.get(ec_url, params=ec_params)

			data = json.loads(ec_r.text)

			for i in range(len(data['response']['songs'])):
				if len(data['response']['songs'][i]['tracks']) > 0:
        				tracks.append(data['response']['songs'][i]['tracks'][0]['foreign_id'][14:])
			first_song = tracks[0]
			tracks.pop[0]
		else:
			form.twitter.data = ""
	return render_template("index.html",
		form = form,
		first_song = first_song,
		tracks = tracks,
		mood = mood)

