from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/welcome/<num1>/<num2>')
def boxes(num1,num2):
	return render_template("index.html", number = int(num1)/int(num2))

if __name__=="__main__":
    app.run(debug = True)
