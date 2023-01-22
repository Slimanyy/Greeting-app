from flask import Flask, render_template, request, flash
#import 

app = Flask(__name__)
app.secret_key = 'dfghjkfcgvbhjmkfcgvhbjk'


@app.route("/hello")
def index():
	flash("What`s your name?")
	return render_template("index.html")


@app.route("/greet", methods=["POST", "GET"])
def greet():
	flash("Hi " + str(request.form['name_input']) + ", great to see you!")
	return render_template("index.html")
