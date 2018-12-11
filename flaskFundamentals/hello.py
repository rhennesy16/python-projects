from flask import Flask, render_template, request  
app = Flask(__name__)    
                         
print(__name__)  

@app.route('/')
def helloWorld():
    return 'Hello World'          
                         
@app.route("/hello/<name>")
def hello(name):
	print("name")
	return "hello"""+name

@app.route('/dojo')
def name():
	return 'dojo'

@app.route('/<input>')
def say(input):
	return f"Hi {input}"

@app.route('/repeat')
def repeat():
	return " hello "*35

@app.route('/repeating')
def repeating():
	return " dogs "*99



if __name__=="__main__": 


    app.run(debug = True)   


