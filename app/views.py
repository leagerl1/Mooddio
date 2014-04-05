from flask import render_template, flash, redirect
from app import app
from forms import LoginForm

@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
def index():
	form = LoginForm()
	posts = [ # fake array of posts
        	{ 
            		'author': { 'nickname': 'John' }, 
	        	'body': 'Beautiful day in Portland!' 
        	},
        	{ 
            		'author': { 'nickname': 'Susan' }, 
            		'body': 'The Avengers movie was so cool!' 
        	}
    	]
	return render_template("index.html",
		form = form,
		posts = posts)
