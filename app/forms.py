from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, HiddenField, RadioField
from db import JsonDB

db = JsonDB('data')
goals = [(goal['id'], goal['title']) for goal in db.all('goals')]


class SortTeachersForm(FlaskForm):
    sort = SelectField(
        'sort',
        choices=(
            ('random', 'В случайном порядке'),
            ('-rating', 'Сначала лучшие по рейтингу'),
            ('price', 'Сначала недорогие'),
            ('-price', 'Сначала дорогие'),
        )
    )


class BookingForm(FlaskForm):
    client_name = StringField('Вас зовут')
    client_phone = StringField('Ваш телефон')
    client_time = HiddenField()
    client_teacher = HiddenField()
    client_weekday = HiddenField()


class RequestForm(FlaskForm):
    goal = RadioField('Какая цель занятий?', choices=goals)
    time = RadioField(
        'Сколько времени есть?',
        choices=[
            ('1-2', '1-2 часа в неделю'),
            ('3-5', '3-5 часов в неделю'),
            ('5-7', '5-7 часов в неделю'),
            ('7-10', '7-10 часов в неделю'),
        ],
    )
    name = StringField('Вас зовут')
    phone = StringField('Ваш телефон')
