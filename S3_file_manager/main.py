from flask import Flask, app

app = Flask(__name__)

@app.route("/")
def main_page():
    return "Hello world"
