from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    info = request.form
    print(request.form)
    print(info)
    return render_template('index2.html', info = info)

@app.route('/danger')
def danger():
    print("A user tried to visit /danger. We redirected the user to /.")
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)
