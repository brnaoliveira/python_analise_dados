from flask import Flask, flash, redirect, render_template, request, session, abort
app = Flask(__name__)


# Cada @app.route é uma página


@app.route("/")
def index():
    return "Flask app"


# Na página /members/name retorna o nome
@app.route("/hello/<string:name>/")
def getMember(name):
    return render_template('template1.html', name=name)


if __name__ == "__main__":
    app.run(host= '0.0.0.0', port = 80)