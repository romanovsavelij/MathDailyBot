from task.database import Database
from task.users_manager import UsersManager


class TaskManager:
    def __init__(self):
        self.users_manager = UsersManager()
        self.database = Database()

    def register_new_user(self, user_id: int):
        ...

    def set_subject(self, user_id: int, subject: str):
        # user wants task of this subject
        ...

    def get_settings(self, user_id: int):
        # subject and level that user chose
        return {}

    def get_statement(self, user_id: int, task_id):
        return 'statement statement statement'

    def get_hint(self, user_id: int, task_id):
        return 'hint hint ... hint hint'

    def get_solution(self, user_id: int, task_id):
        return 'solution solution ... solution solution'

    def get_task(self, user_id: int):
        settings = self.get_settings(user_id)
        tasks = self.database.get_tasks(settings)
        # check that user hasn't already solved this problem
        task = tasks[0]
        title = f'**{task.get_name()}**'
        statement = task.get_statement()
        return f'{title}\n\n{statement}'