import os
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

SECRET_KEY = os.urandom(32)
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY




# Форма аутентификации

class AuthForm(FlaskForm):
    login = StringField('Ваш логин')
    passwd = PasswordField('Ваш пароль')
    submit = SubmitField('Вход в систему')


@app.route('/')
def index():
    form = AuthForm()

    login = form.login.data
    passwd = form.passwd.data

    return render_template("index.html", form=form)


app.run('0.0.0.0', debug=True)
