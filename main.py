from flask import Flask
import subprocess


app = Flask(__name__)


@app.route('/')
def index():
    result = subprocess.run(["pyjoke"], stdout=subprocess.PIPE)
    number_of_jokes = "\"number of jokes\""
    return f'<h1>welcome to my flask app that gets deployed by github actions</h1> <img src="https://github.com/Sander-317/cd_pipline/actions/workflows/run-test.yml/badge.svg" alt="badge"> <div><h1>Joke<h1><h2>{result.stdout.decode("utf-8")}<h2><h3>hit refresh to refresh the joke</h3><h3>if you need more jokes go to http://157.230.19.4/jokes/{number_of_jokes} and you get all the jokes you want  </div>'

@app.route('/jokes/<number>')
def get_jokes(number):
    try:
        joke_list = []
        for i in range(int(number)):
             result = subprocess.run(["pyjoke"], stdout=subprocess.PIPE)
             joke_list.append(result.stdout.decode("utf-8"))
    except:
        return "<h1>the end of the url must be a number</h1>"

    test = [f"{joke}" for joke in joke_list ]
    
    return f'<ol><h1>{number} jokes list</h1>{[f"<li><h2>{joke[:-2]}</h2> </li> " for joke in joke_list ]}</ol>'
    

if __name__ == '__main__':
    app.run( "0.0.0.0", debug=True)