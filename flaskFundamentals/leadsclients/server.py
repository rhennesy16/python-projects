
from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL

app = Flask(__name__)
mysql = connectToMySQL('friendsdb')
print("all the users", mysql.query_db("SELECT * FROM friends;"))

@app.route('/')
def index():
    mysql = connectToMySQL("friendsdb")
    all_friends = mysql.query_db("SELECT * FROM friends")
    print("Fetched all friends", all_friends)
    return render_template('index.html', friends = all_friends)

@app.route('/create_friend', methods=['POST'])
def create():
    print(request.form)
    mysql = connectToMySQL("friendsdb")
    query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(occupation)s, NOW(), NOW());"
    data = {
             'customer_name': request.form['CustomerName'],
             'Number_of_new_leads':  request.form['leads']
           }
    new_friend_id = mysql.query_db(query, data)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)