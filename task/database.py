from typing import Dict, List
from airtable import Airtable
from task.task import Task


class Database:
    def __init__(self):
        self.table = Airtable('appffcIXRvvuxka4B', 'Problems',
                              api_key='keyZfwZUbtTad4m4q')

    def get_tasks(self, user_task_settings: Dict[str]) -> List[
        Task]:  # Task settings is a dictionary {Subject: {}, Level: {}}
        tasks = []
        for task in self.table.get_all():
            data = task['fields']
            if 'Statement' in data and 'Solution' in data and 'Subject' in data and \
                    'Name' in data and 'Level' in data and 'Hint' in data:  # Not necessary to check as all the fields are non-empty
                if data['Subject'] == user_task_settings['Subject'] and \
                        data['Level'] == user_task_settings['Level']:
                    tasks.append(Task(data['Name'], data['Statement'],
                                      data['Solution'], data['Hint'],
                                      data['Level'], data['Subject']))
        return tasks
