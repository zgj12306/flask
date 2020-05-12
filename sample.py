from flask import Blueprint
sample = Blueprint('sample',__name__)

@sample.route('/')
@sample.route('/hello')
def index():
	return "This page is a blueprint page"
