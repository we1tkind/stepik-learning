from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/all/')
def all_profiles():
    return render_template('all.html')


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
