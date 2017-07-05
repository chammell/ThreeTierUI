import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return 'Hello from Flaskapp'

@app.route('/home', methods=['GET', 'POST'])
def home():
	return render_template('example.html')

@app.route('/last', methods=['GET', 'POST'])
def last():
	return requests.get('http://ec2-34-204-7-184.compute-1.amazonaws.com/getlast').content
	
if __name__ == '__main__':
	app.run(debug=True)
