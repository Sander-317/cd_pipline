# Import what we need from flask
from flask import Flask

# Create a Flask app inside `app`
app = Flask(__name__)

# Assign a function to be called when the path `/` is requested
@app.route('/')
def index():
    return '<h1>welcome to my flask app that gets deployed by github actions</h1> [![Run Tests and deploy](https://github.com/Sander-317/cd_pipline/actions/workflows/run-test.yml/badge.svg)](https://github.com/Sander-317/cd_pipline/actions/workflows/run-test.yml/badge.svg) '

@app.route('/test')
def cow():
    return 'it still works'


if __name__ == '__main__':
    app.run( "0.0.0.0", debug=True)