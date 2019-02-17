from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Joshua'}
	entries = [
	    {
	        'author': {'username': 'John'},
	        'content': 'Today is a wonderful today'
	    },
	    {
	        'author': {'username': 'John'},
	        'content': 'Yesterday was good also'	        
	    }
	]
	return render_template('index.html', title='Home', user=user, entries=entries)

@app.route('/about')
def about():
	return render_template('about.html', title='About')

@app.route('/login')
def login():
	form = LoginForm()
	return render_template('login.html', title='Sign In', form=form)