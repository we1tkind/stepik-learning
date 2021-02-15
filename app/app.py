import os

from flask import Flask, render_template, request

from db import JsonDB
from forms import SortTeachersForm
from filters import word_agree_with_number

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'secret')
app.jinja_env.filters['word_agree_with_number'] = word_agree_with_number

db = JsonDB('data/')


@app.route('/')
def index():
    teachers = db.all('teachers', limit=6)
    return render_template('index.html', teachers=teachers)


@app.route('/all/', methods=['GET', 'POST'])
def all_profiles():
    sort = None
    form = SortTeachersForm()
    if request.method == 'POST':
        sort = form.sort.data
    teachers = db.all('teachers', sort=sort)
    return render_template('all.html', teachers=teachers, form=form)


@app.route('/profiles/<int:profile_id>')
def profile(profile_id):
    return render_template('profile.html')


@app.route('/goals/<goal>')
def goals(goal):
    return render_template('goal.html')


@app.route('/request/')
def request():
    return render_template('request.html')


@app.route('/request_done/')
def request_done():
    return render_template('request_done.html')


@app.route('/booking/<int:profile_id>/<weekday>/<time>/')
def booking():
    return render_template('booking.html')


@app.route('/booking_done/')
def booking_done():
    return render_template('booking_done.html')


if __name__ == '__main__':
    app.run(debug=True)
