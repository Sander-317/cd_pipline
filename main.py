# Import what we need from flask
from flask import Flask
import datetime

# date = datetime.datetime.now()
# print(date)
# print(date.format('YYYY-MM-DD hh:mm:ss'))

# Create a Flask app inside `app`
app = Flask(__name__)

# Assign a function to be called when the path `/` is requested
@app.route('/')
def index():
    return 'nog een test '

@app.route('/cow')
def cow():
    return 'MOoooOo!'


if __name__ == '__main__':
    app.run( "0.0.0.0", debug=True)