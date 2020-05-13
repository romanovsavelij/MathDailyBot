from typing import Dict, List
from airtable import Airtable
from task.task import Task
from keys import AIRTABLE_API_KEY, AIRTABLE_ID


class Database:
    def __init__(self):
        self.table = Airtable(AIRTABLE_ID, 'Problems', api_key=AIRTABLE_API_KEY)

    def get_tasks(self, user_task_settings) -> List[Task]:
        # Task settings is a dictionary {Subject: {}, Level: {}}
        tasks = []
        for task in self.table.get_all():
            data = task['fields']
            if data == {}:
                continue
            if 'Level' in user_task_settings and not data['Level'] == user_task_settings['Level']:
                continue
            if 'Subject' in user_task_settings and not data['Subject'] == user_task_settings['Subject']:
                continue
            if 'Statement' in data and 'Solution' in data and 'Subject' in data and \
                    'Name' in data and 'Level' in data and 'Hint' in data:
                tasks.append(Task(data['Name'], data['Statement'], data['Solution'],
                                  data['Hint'], data['Level'], data['Subject']))
        return tasks
