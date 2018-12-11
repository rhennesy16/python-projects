from flask import Flask, session, flash, render_template, request, redirect
from mysqlconnection import connectToMySQL
import re
app = Flask(__name__)
app.secret_key = 'key'

NAME_REGEX = re.compile(r'^[a-zA-Z`~]+$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')



mysql = connectToMySQL('')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/new_registration', methods=['POST'])
def email():
	mysql = connectToMySQL('registrationdb')
	all_registrations = mysql.query_db('SELECT * FROM registration')
	print(request.form)
	if len(request.form['first_name']) < 2 or > 15:
		flash("First name must contain atleast 2 letters and contain only letters")
	elif not NAME_REGEX.match(request.form['first_name']):
		flash("First name must contain atleast 2 letters and contain only letters")
	else:
		flash("Good")
	mysql = connectToMySQL("registrationdb")
	query = "INSERT INTO registration (email, created_at, updated_at) VALUES (%(email)s, NOW(), NOW());"
	data = {
			'email': request.form['email']
			}	

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/')
def index():
	return render_template('index.html')


if __name__ == "__main__":
	app.run(debug=True)