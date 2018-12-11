from flask import Flask  # Import Flask to allow us to create our app.

app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file

@app.route('/')
@app.route('/<name>')
def index(name="Reggie"):
	name = request.args.get('name', name)
	return "Hello from {}".format(name)


@app.route('/add/<int:num1>/<int:num2>')
def add(num1,num2):
	return '{} + {} = {}'.format(num1,num2,num1+num2)

app.run(debug=True, port=5000, host='0.0.0.0')