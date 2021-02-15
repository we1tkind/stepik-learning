from typing import Optional
import json
from pathlib import Path
import random


class JsonDB:

    def __init__(self, dir_name):
        self.dir_name = Path(dir_name)

    def get(self, collection: str, instance_id: int) -> dict:
        file_path = self.dir_name.joinpath(collection, f'{instance_id}.json')
        with open(file_path, 'r') as json_file:
            return json.loads(json_file.read())

    def all(self, collection: str, limit: Optional[int] = -1,
            sort: str = 'random'):
        instances = []
        files = list(self.dir_name.joinpath(collection).glob('*.json'))
        if sort == 'random':
            random.shuffle(files)
        for file in files:
            with open(file, 'r') as json_file:
                instances.append(json.loads(json_file.read()))
        return instances[:limit]

    def write(self):
        pass
