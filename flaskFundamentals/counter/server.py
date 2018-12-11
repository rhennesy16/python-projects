from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key="no"

@app.route('/')
def home():
    if 'count' in session:
        session['count']=session['count'] +1
    else:
        session['count']=1
    return render_template('index.html')

@app.route('/count', methods=['POST'])
def count():
    if 'count' in session:
        session['count']=session['count'] +1
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)
