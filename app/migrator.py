"""Переносит данные из файла data.py в базу данных на основе json файлов."""
from pathlib import Path
import json

from data import goals, teachers


def migrate(file_path, data):
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, 'w', encoding='utf8') as f:
        json.dump(data, f, indent=4, sort_keys=False, ensure_ascii=False)


def migrate_teachers(path, teachers):
    for teacher in teachers:
        file_path = path.joinpath('teachers', f'{teacher["id"]}.json')
        migrate(file_path, teacher)


def migrate_goals(path, goals):
    file_path = path.joinpath('goals.json')
    emoji = iter('⛱🏫🏢🚜🖥️')
    migrate(
        file_path,
        {'goals': [
            {'id': k, 'title': v, 'emoji': next(emoji)}
            for k, v in goals.items()
        ]})


def migrate_all():
    path = Path('data/')
    migrate_goals(path, goals)
    migrate_teachers(path, teachers)


if __name__ == '__main__':
    migrate_all()
