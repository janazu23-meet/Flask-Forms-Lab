from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "jana"
password = "456"
facebook_friends=["Yasmin","Mayar","Jimin", "George", "Fouad", "Celina"]


@app.route('/' , methods=['POST', 'GET'])
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		username1 = request.form['username']
		password1 = request.form['password']
	if username1 == username and password1 == password:
		return redirect(url_for('home'))

@app.route('/home')
def home():
	return render_template('home.html', facebook_friends = facebook_friends)

@app.route('/friend_exists/<string:name>', methods=['POST', 'GET'])
def friend_exists(name):
	return render_template('friend_exists.html', n = name, facebook_friends = facebook_friends)



if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)