import os

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'YjZm7YTM3zOWRkODJlNz1BjYWUyY3jY5M4jBm'
