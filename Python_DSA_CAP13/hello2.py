from flask import Flask
app = Flask(__name__)


# Cada @app.route é uma página

# Retorna Index
@app.route("/")
def index():
    return "Index"

# Na página /hello retorna o Hello world
@app.route("/hello")
def hello():
    return "Hello World"

# Na página /members retorna o members
@app.route("/members")
def members():
    return "Members"

# Na página /members/name retorna o nome
@app.route("/members/<string:name>/")
def getMember(name):
    return name


if __name__ == "__main__":
    app.run()