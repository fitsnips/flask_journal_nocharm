import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'YjZm7YTM3zOWRkODJlNz1BjYWUyY3jY5M4jBm'
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
	    'sqlite:///' + os.path.join(basedir, 'app.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
