from flask import Flask, session, flash, render_template, request, redirect
from mysqlconnection import connectToMySQL
import re
app = Flask(__name__)
app.secret_key = 'key'

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


mysql = connectToMySQL('registrationdb')
print("all the emails", mysql.query_db("SELECT * FROM registration;"))

@app.route('/')
def index():
	mysql = connectToMySQL("registrationdb")
	all_emails = mysql.query_db("SELECT * FROM registration;")
	return render_template('index.html', emails = all_emails)

@app.route('/new_email', methods=['POST'])
def email():
	mysql = connectToMySQL('emailsdb')
	all_emails = mysql.query_db('SELECT * FROM registration')
	print(request.form)
	if len(request.form['email']) < 1:
		flash("Email cannot be blank!")
	elif not EMAIL_REGEX.match(request.form['email']):
		flash("Invalid Email Address!")
	else:
		flash("Success!")
	mysql = connectToMySQL("emailsdb")
	query = "INSERT INTO registration (email, created_at, updated_at) VALUES (%(email)s, NOW(), NOW());"
	data = {
			'email': request.form['email']
			}
	mysql.query_db(query,data)
	return redirect('/')

if __name__ == "__main__":
	app.run(debug=True)