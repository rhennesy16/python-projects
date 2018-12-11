
from flask import Flask, render_template, request
from mysqlconnection import connectToMySQL

app = Flask(__name__)
mysql = connectToMySQL('')


if __name__ == "__main__":
    app.run(debug=True)