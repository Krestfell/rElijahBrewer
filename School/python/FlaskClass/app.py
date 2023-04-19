# mainController.py
from flask import Flask
from flask import renderTemplate


app = Flask(__name__)

@app.route("/") #decorator
def helloWorld():
    return "Hello, Flask!"

@app.route("/about")
def about():
    return "Welcome to Flask!"

@app.route("/concat/<firstName>")
@app.route("/concat/<firstName>/<lastName>")

def concat(firstName=None, lastName=None):
    if(lastName):
        return '<B>hello</B>' + firstName.capitalize() + ' ' + lastName.capitalize()
    else:
        return '<I>hello</I>' + 