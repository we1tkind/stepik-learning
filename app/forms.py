from flask_wtf import FlaskForm
from wtforms import RadioField


class SortTeachersForm(FlaskForm):
    sort = RadioField(
        'sort',
        choices=(
            ('random', 'В случайном порядке'),
            ('rating', 'Сначала лучшие по рейтингу'),
            ('price', 'Сначала недорогие'),
            ('-price', 'Сначала дорогие'),
        )
    )
