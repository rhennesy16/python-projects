from flask import Flask  # Import Flask to allow us to create our app.
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file
                         # directly, or importing it as a module.
app = Flask (__name__)
app.run(debug=True, port=5000, host='0.0.0.0')