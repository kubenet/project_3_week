import json
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import RadioField, TextField

app = Flask(__name__)
app.secret_key = 'key'

with open('data.json', 'r') as r:
    all_data = json.load(r)
    r.close()


# Запись нового запроса в файл all_requests.json
def add_request(name, phone, goal, times):
    with open('all_requests.json', 'r') as r:
        records = json.load(r)
    records.append({'name': name, 'phone': phone, 'goal': goal, 'times': times})
    r.close()
    with open('all_requests.json', 'w') as w:
        json.dump(records, w)
    w.close()


# Запись нового запроса в файл all_requests.json
def update_timtale_teacher(id_teacher, day, times):
    with open('data.json', 'r') as r:
        records = json.load(r)
        records[1][int(id_teacher)]['free'][day][times] = False
        r.close()

    with open('data.json', 'w') as w:
        json.dump(records, w)
        w.close()
    with open('data.json', 'r') as r:
        global all_data
        all_data = json.load(r)
        r.close()


def update_data():
    with open('data.json', 'r') as r:
        global all_data
        all_data = json.load(r)
        r.close()
    # for day in all_data[1][0]['free']:
    #     print(day)
    #     for key in all_data[1][0]['free'][day]:
    #         if all_data[1][0]['free'][day][key]:
    #             print(key)


update_data()


class RequestForm(FlaskForm):  # объявление класса формы для WTForms
    name = TextField('name')
    phone = TextField('phone')
    goal = RadioField("Какая цель занятий?", choices=[('0', 'Для путешествий'), ('1', 'Для школы'), ('2', 'Для работы'),
                                                      ('3', 'Для переезда')])
    time = RadioField("Сколько времени есть?",
                      choices=[('0', '1-2 часа в неделю'), ('1', '3-5 часов в неделю'), ('2', '5-7 часов в неделю'),
                               ('3', '7-10 часов в неделю')])


@app.route('/')  # главная
def index():
    return render_template("index.html", all_data=all_data)


@app.route('/techers/')  # все репетиторы
def techers():
    return render_template("techers.html", all_data=all_data)


@app.route('/goals/<goal>/')  # здесь будет цель <goal>
def goals(goal):
    return render_template("goals.html", goal=goal, all_data=all_data)


@app.route('/profiles/<int:id_techers>/')  # здесь будет преподаватель <id учителя>
def profiles(id_techers):
    return render_template("profiles.html", id_techers=id_techers, all_data=all_data)


@app.route('/requests/')  # здесь будет заявка на подбор
def requests():
    ReqForm = RequestForm()  # Форма для страницы ('/request')
    return render_template("request.html", form=ReqForm, all_data=all_data)


@app.route('/request_done/', methods=['POST'])  # заявка на подбор отправлена
def request_done():
    form = RequestForm()
    name = form.name.data
    phone = form.phone.data
    goal = form.goal.data
    times = form.time.data

    goal_choices = {'0': 'Для путешествий', '1': 'Для школы', '2': 'Для работы', '3': 'Для переезда'}
    time_choices = {'0': '1-2 часа в неделю', '1': '3-5 часов в неделю', '2': '5-7 часов в неделю',
                    '3': '7-10 часов в неделю'}

    add_request(name, phone, goal_choices[goal], time_choices[times])
    return render_template("request_done.html", username=name, userphone=phone, goal=goal_choices[goal],
                           time=time_choices[times])


@app.route('/booking/<int:id_techers>/<day>/<time>/')  # здесь будет форма бронирования <id учителя>
def booking(id_techers, day, time):
    return render_template("booking.html", id_techers=id_techers, day=day, time=time, all_data=all_data)


@app.route('/booking_done/', methods=['POST'])  # заявка отправлена
def booking_done():
    clientWeekday = request.form["clientWeekday"]
    clientTime = request.form["clientTime"]
    clientTeacher = request.form["clientTeacher"]
    clientName = request.form["clientName"]
    clientPhone = request.form["clientPhone"]

    update_timtale_teacher(clientTeacher, clientWeekday,
                           clientTime)  # Обновляем расписание свободного времени репетитора
    update_data()
    return render_template("booking_done.html", clientName=clientName, clientPhone=clientPhone, clientTime=clientTime,
                           clientTeacher=clientTeacher, clientWeekday=clientWeekday)


app.run('0.0.0.0', debug=True)
