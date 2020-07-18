import json
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

app = Flask(__name__)


with open('data.json', 'r') as r:
    all_data = json.load(r)
    r.close()
# #print(all_data[0])
# for key in all_data[1]:
#     if 'work' in key['goals']:
#         print(key['name'])

@app.route('/') # главная
def index():
    return render_template("index.html", all_data=all_data)

@app.route('/techers/') # все репетиторы
def techers():
    return render_template("techers.html", all_data=all_data)

@app.route('/goals/<goal>/')    # здесь будет цель <goal>
def goals(goal):
    return render_template("goals.html", goal=goal, all_data=all_data)

@app.route('/profiles/<int:id_techers>/')   #  здесь будет преподаватель <id учителя>
def profiles(id_techers):
    return render_template("profiles.html", id_techers=id_techers, all_data=all_data)

@app.route('/request/')     # здесь будет заявка на подбор
def request():
    return render_template("request.html")

@app.route('/request_done/', methods=['POST'])    # заявка на подбор отправлена
def request_done():
    return render_template("request_done.html")

@app.route('/booking/<int:id_tesachers>/<int:day>/<time>/') # здесь будет форма бронирования <id учителя>
def booking():
    return render_template("booking.html")

@app.route('/booking_done/')    # заявка отправлена
def booking_done():
    return render_template("booking_done.html")


app.run('0.0.0.0', debug=True)
