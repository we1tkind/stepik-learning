"""Переносит данные из файла data.py в базу данных на основе json файлов."""
from pathlib import Path
import json

from data import goals, teachers


def migrate(file_path, data):
    with open(file_path, 'w', encoding='utf8') as f:
        json.dump(data, f, indent=4, sort_keys=True, ensure_ascii=False)


def migrate_all():
    data_dict = {'goals': goals, 'teachers': teachers}
    path = Path('data/')
    path.mkdir(parents=True, exist_ok=True)
    for filename, data in data_dict.items():
        file_path = path.joinpath(f'{filename}.json')
        migrate(file_path, {filename: data})


if __name__ == '__main__':
    migrate_all()
