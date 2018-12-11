from flask import Flask, render_template
app = Flask (__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/welcome/<num>')
def boxes(num):
	return render_template("index.html", number = int(num))

@app.route('/welcome/<x>,<color>')
def boxes(x,color):
	return render_template("index.html", number = int(num), hue = color)

@app.route('/welcome/<num>')
def boxes(num):
	return render_template("index.html", number = int(num))



if __name__=="__main__": 
    app.run(debug = True)   
