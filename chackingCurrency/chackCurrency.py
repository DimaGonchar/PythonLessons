from flask import Flask
import requests
import json
app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Hello!</h1>"

if __name__ == "__main__":
    app.run(debug=True)






