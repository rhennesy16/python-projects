from flask import Flask, render_template, request, redirect, session, flash, url_for
import re
from flask_bcrypt import Bcrypt
from mysqlconnection import MySQLConnection

app = Flask(__name__)
app.secret_key = 'secret'
mysql = MySQLConnection('registrationdb')
bcrypt = Bcrypt(app)

emailRegex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
passwordRegex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$')

def validate():
    errors = 0
    #Check first name
    if request.form['first_name'] == '':
        flash('Name cannot be blank', 'first_nameError')
        errors += 1
        pass
    elif any(char.isdigit() for char in request.form['first_name']) == True:
        flash('Name cannot have numbers', 'first_nameError')
        errors += 1
        pass
    else:
        session['first_name'] = request.form['first_name']
    #Check last name
    if request.form['last_name'] == '':
        flash('Name cannot be blank', 'lastNameError')
        errors += 1
        pass
    elif any(char.isdigit() for char in request.form['last_name']) == True:
        flash('Name cannot have numbers', 'lastNameError')
        errors += 1
        pass
    else:
        session['last_name'] = request.form['last_name']
    #Check email
    if request.form['email'] == '':
        flash('Email cannot be blank', 'emailError')
        errors += 1
        pass
    elif not emailRegex.match(request.form['email']):
        flash('Invalid email address', 'emailError')
        errors += 1
        pass
    else:
        session['email'] = request.form['email']
    #Check password
    if request.form['password'] == '':
        flash('Password cannot be blank', 'passwordError')
        errors += 1
        pass
    elif len(request.form['password']) < 8:
        flash('Password must be greater than 8 characters', 'passwordError')
        errors += 1
        pass
    elif not passwordRegex.match(request.form['password']):
        flash('Password must contain at least one lowercase letter, one uppercase letter, and one digit', 'passwordError')
        errors += 1
        pass
    else:
        session['password'] = request.form['password']
    #Check confirmation password
    if request.form['confirm_password'] == '':
        flash('Please confirm password', 'confirmPasswordError')
        errors += 1
        pass
    elif request.form['confirm_password'] != request.form['password']:
        flash('Passwords do not match', 'confirmPasswordError')
        errors += 1
    else:
        session['confirm_password'] = request.form['confirm_password']
    #See if there are any errors
    if errors > 0:
        session['password'] = ''
        session['confirm_password'] = ''
        return False
    else:
        return True

def validateLogin():
    errors = 0
     #Check email
    if request.form['email'] == '':
        flash('Email cannot be blank', 'emailError')
        errors += 1
        pass
    elif not emailRegex.match(request.form['email']):
        flash('Invalid email address', 'emailError')
        errors += 1
        pass
    else:
        session['email'] = request.form['email']
    #Check password
    if request.form['password'] == '':
        flash('Password cannot be blank', 'passwordError')
        errors += 1
        pass
    elif len(request.form['password']) < 8:
        flash('Password must be greater than 8 characters', 'passwordError')
        errors += 1
        pass
    elif not passwordRegex.match(request.form['password']):
        flash('Password must contain at least one lowercase letter, one uppercase letter, and one digit', 'passwordError')
        errors += 1
        pass
    else:
        session['password'] = request.form['password']
        #See if there are any errors
    if errors > 0:
        session['password'] = ''
        session['confirmPassword'] = ''
        return False
    else:
        return True

@app.route('/')
def index():
    if 'first_name' not in session:
        session['first_name'] = ''
    if 'last_name' not in session:
        session['last_Name'] = ''
    if 'email' not in session:
        session['email'] = ''
    if 'password' not in session:
        session['password'] = ''
    if 'confirm_password' not in session:
        session['confirm_password'] = ''
    if 'user_id' not in session:
        session['user_id'] = ''
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create():
    if validate() == False:
        return redirect('/')
    else:
        encryptedPassword = bcrypt.generate_password_hash(request.form['password'])
        data = {
                'first_name': request.form['first_name'],
                'last_name': request.form['last_name'],
                'email': request.form['email'],
                'password': encryptedPassword
                }
        query = "INSERT INTO registration (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s, NOW(), NOW());"
        mysql.query_db(query, data)
        session['password'] = ''
    return redirect('/dashboard')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/validate', methods=['POST'])
def validateLoginInfo():
    if validateLogin() == False:
        return redirect('/login')
    else:
        data = {
                'email': request.form['email']
        }
        mysql = MySQLConnection('registrationdb')
        query = "SELECT * FROM registration WHERE email = %(email)s"
        userInfo = mysql.query_db(query, data)
        print(userInfo)
        if len(userInfo)>0:
        # inputPassword = request.form['password']
            inputPasswordEncrypted = bcrypt.check_password_hash(userInfo[0]['password'],request.form['password'])
        if inputPasswordEncrypted == True:
            return redirect('/dashboard')
        else:
            flash('Incorrect password', 'passwordError')
    return redirect('/login')

@app.route('/dashboard')
def returnDashboard():
    if session['email']:
        return render_template('dashboard.html')
    else:
        return redirect('/')

@app.route('/logout', methods=['POST'])
def clear():
    session['first_Name'] = ''
    session['last_Name'] = ''
    session['email'] = ''
    session['password'] = ''
    session['confirm_password'] = ''
    session['userid'] = ''
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)