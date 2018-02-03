from flask import Flask, render_template, request, session, redirect, flash, url_for
import os, sqlite3

app = Flask(__name__)
app.secret_key = os.urandom(32)


@app.route("/")
def main():
	return render_template("home.html", name="MicroSoft Band 2")


@app.route("/thing1")
def thing1():
	return render_template("home.html", name="thing1")


@app.route("/thing2")
def thing2():
	return render_template("home.html", name="thing2")


if __name__ == "__main__":
	app.debug = True
	app.run()
