from typing import List, Dict

from task.task import Task


class User:
    def __init__(self, user_id: int):  # initialize with a list of tasks
        # from database
        self.id = user_id

        self.settings = Dict[str, str]
        self.settings = {'Subject': '', 'Level': ''}

        self.given_tasks = List[Task]
        self.solved_tasks = List[Task]

    def give_task(self, task: Task):
        self.given_tasks.append(task)

    def solved_task(self, task: Task):
        self.solved_tasks.append(task)

    def is_solved(self, task: Task):
        return task in self.solved_tasks

    def get_given_tasks(self):
        return self.given_tasks

    def get_solved_tasks(self):
        return self.solved_tasks  # just in case

    def get_settings(self):
        return self.settings

    def set_settings_Subject(self, subject: str):
        self.settings['Subject'] = subject

    def set_settings_Level(self, level: str):
        self.settings['Level'] = level

    def get_user_id(self):
        return self.id
