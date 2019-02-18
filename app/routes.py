from flask import render_template, flash, redirect, url_for
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

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for user {}, remember_me={}'.format(
			form.username.data, form.remember_me.data))
		return redirect(url_for('index'))
	return render_template('login.html', title='Sign In', form=form)