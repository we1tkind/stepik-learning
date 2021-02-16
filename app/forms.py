from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, HiddenField


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
