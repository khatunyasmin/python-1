"""from flask import Flask,render_template
app=Flask(__name__)

@app.route("/")
def hello():
    return "welcome to yasmin"

@app.route("/about")
def bye():
    return "welcome to apni duniya"


app.run()"""
from flask import Flask ,render_template

app=Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

app.run()