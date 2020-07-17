import os
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


app.run('0.0.0.0', debug=True)
