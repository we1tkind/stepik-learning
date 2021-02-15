from typing import Optional
import json
from pathlib import Path
import random
from operator import itemgetter


class JsonDB:

    def __init__(self, dir_name):
        self.dir_name = Path(dir_name)

    def get(self, collection: str, instance_id: int) -> dict:
        file_path = self.dir_name.joinpath(collection, f'{instance_id}.json')
        with open(file_path, 'r') as json_file:
            return json.loads(json_file.read())

    @staticmethod
    def sort(instances: list, sort: str = None) -> list:
        sort = sort or 'random'
        reverse = False
        if sort[0] == '-':
            reverse = True
            sort = sort[1:]
        if sort == 'random':
            random.shuffle(instances)
            return instances
        return sorted(instances, key=itemgetter(sort), reverse=reverse)

    @staticmethod
    def filter(instances: list, filters: Optional[dict] = None) -> list:
        if filters:
            for k, v in filters.items():
                instances = filter(lambda x: x[k] == v, instances)
        return list(instances)

    def all(self, collection: str, limit: Optional[int] = -1,
            sort: str = 'random', filters: Optional[dict] = None):
        instances = []
        files = list(self.dir_name.joinpath(collection).glob('*.json'))
        for file in files:
            with open(file, 'r') as json_file:
                instances.append(json.loads(json_file.read()))
        instances = self.filter(instances, filters)
        instances = self.sort(instances, sort)
        return instances[:limit]

    def update(self, collection: str, instance_id: int, updated_data: dict):
        pass
