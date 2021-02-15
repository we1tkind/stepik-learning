from flask_wtf import FlaskForm
from wtforms import SelectField


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
