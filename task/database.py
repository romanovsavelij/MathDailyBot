from typing import Dict, List
from airtable import Airtable
from task.task import Task


class Database:
    def __init__(self):
        self.table = Airtable('appffcIXRvvuxka4B', 'Problems', api_key='keyZfwZUbtTad4m4q')

    def get_tasks(self, settings: Dict) -> List[Task]:
        tasks = []
        for task in self.table.get_all():
            data = task['fields']
            if data == {}:
                continue
            if 'Level' in settings and not data['Level'] == settings['Level']:
                continue
            if 'Subject' in settings and not data['Subject'] == settings['Subject']:
                continue
            if 'Statement' in data and 'Solution' in data and 'Subject' in data and \
                    'Name' in data and 'Level' in data and 'Hint' in data:
                tasks.append(Task(data['Name'], data['Statement'], data['Solution'],
                                  data['Hint'], data['Level'], data['Subject']))
        return tasks
