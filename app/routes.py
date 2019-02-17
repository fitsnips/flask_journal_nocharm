from flask import render_template
from app import app

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
