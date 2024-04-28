# from flask import Flask
# app = Flask(__name__)
from flask_app import app

from flask_app.controllers import testing

if __name__=="__main__":
    app.run(debug=True)