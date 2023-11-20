# Import what we need from flask
from flask import Flask
import subprocess

# Create a Flask app inside `app`
app = Flask(__name__)

# Assign a function to be called when the path `/` is requested
@app.route('/')
def index():
    result = subprocess.run(["pyjoke"], stdout=subprocess.PIPE)
    return f'<h1>welcome to my flask app that gets deployed by github actions</h1> <img src="https://github.com/Sander-317/cd_pipline/actions/workflows/run-test.yml/badge.svg" alt="badge"> <div><h1>Joke<h1><br><h2>{result.stdout.decode("utf-8")}<h2></div>'

@app.route('/test')
def cow():
    return 'it still works test again'


if __name__ == '__main__':
    app.run( "0.0.0.0", debug=True)