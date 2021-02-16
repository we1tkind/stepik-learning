import os

from flask import Flask, render_template, request

from db import JsonDB
from forms import SortTeachersForm, BookingForm
from filters import word_agree_with_number, translate_weekday

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'secret')
app.jinja_env.filters['word_agree_with_number'] = word_agree_with_number
app.jinja_env.filters['translate_weekday'] = translate_weekday

db = JsonDB('data/')
learning_goals = db.all('goals')


@app.route('/')
def index():
    teachers = db.all('teachers', limit=6)
    return render_template(
        'index.html', teachers=teachers, goals=learning_goals,
    )


@app.route('/all/', methods=['GET', 'POST'])
def all_profiles():
    sort = None
    form = SortTeachersForm()
    if request.method == 'POST':
        sort = form.sort.data
    teachers = db.all('teachers', sort=sort)
    return render_template('all.html', teachers=teachers, form=form)


@app.route('/profiles/<int:profile_id>/')
def profile(profile_id):
    teacher = db.get('teachers', profile_id)
    return render_template('profile.html', teacher=teacher)


@app.route('/goals/<goal_id>/')
def goals(goal_id):
    goal = next(
        iter([goal for goal in learning_goals if goal['id'] == goal_id]), None
    )
    teachers = db.all('teachers', filters={'goals': goal['id']}, sort='-rating')
    return render_template('goal.html', goal=goal, teachers=teachers)


@app.route('/request/')
def request_():
    return render_template('request.html')


@app.route('/request_done/')
def request_done():
    return render_template('request_done.html')


@app.route('/booking/<int:profile_id>/<weekday>/<time>/')
def booking(profile_id, weekday, time):
    teacher = db.get('teachers', profile_id)
    form = BookingForm()
    return render_template(
        'booking.html', teacher=teacher, weekday=weekday, time=time, form=form,
    )


@app.route('/booking_done/', methods=['POST'])
def booking_done():
    form = BookingForm()
    time = form.client_time.data
    weekday = form.client_weekday.data
    name = form.client_name.data
    phone = form.client_phone.data
    data = dict(time=time, weekday=weekday, name=name, phone=phone)
    db.create('bookings', data)
    return render_template('booking_done.html', **data)


if __name__ == '__main__':
    app.run(debug=True)
