from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user, logout_user
form app.models import User

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
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user is None or not user.check_password(form.password.data):
			flash('Invalid username or password')
			return redirect(url('login'))
		login_user(user, remember=form.remember_me.data)
		return redirect(url_for('index'))
	return render_template('login.html', title='Sign in', form=form)

@app.route('logout')
def logout():
	logout_user()
	return redirect(url_for('index'))