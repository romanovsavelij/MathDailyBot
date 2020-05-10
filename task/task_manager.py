from typing import Tuple

from task.database import Database
from task.users_manager import UsersManager
from task.user import User


class TaskManager:
    def __init__(self):
        self.users_manager = UsersManager()
        self.database = Database()

    def register_new_user(self, user_id: int):
        new_user = User(user_id)
        self.users_manager.add_user(new_user)

    def set_subject(self, user_id: int, subject: str):
        self.users_manager.user_by_id(user_id).set_settings_Subject(subject)

    def set_level(self, user_id: int, level: str):
        self.users_manager.user_by_id(user_id).set_settings_Level(level)

    def get_settings(self, user_id: int):
        return self.users_manager.user_by_id(user_id).user.get_settings()

    def get_statement(self, user_id: int):
        user = self.users_manager.user_by_id(user_id)
        list_of_all_tasks = self.database.get_tasks(user.get_settings())
        list_of_not_given_tasks = [i for i in list_of_all_tasks if
                                   i not in user.get_given_tasks()]
        if not list_of_not_given_tasks:  # Making sure there are problems satisfying his criteria
            return 'I\'m sorry, there are no problems to meet your criteria. I could suggest something else'
        else:
            return list_of_not_given_tasks[
                0].get_statement()  # The first in the list

    def get_hint(self, user_id: int):
        if not self.users_manager.user_by_id(
                user_id).get_given_tasks():  # At least one task has been given
            return "Attempted to get a hint before the problem was given"
        return self.users_manager.user_by_id(
            user_id).get_given_tasks()[-1].ask_for_hint()

    def get_solution(self, user_id: int):
        assert self.users_manager.user_by_id(
            user_id).get_given_tasks()  # At least one task has been given
        return self.users_manager.user_by_id(user_id).get_given_tasks()[
            -1].get_solution()

    def get_task(self, user_id: int) -> Tuple[str, str]:
        # Returns statement and task id
        settings = self.users_manager.user_by_id(user_id).get_settings()
        tasks = [i for i in self.database.get_tasks(settings) if
                 not self.users_manager.user_by_id(user_id).is_solved()]
        # now we have a list of tasks which meet all the criteria
        if not self.users_manager.user_by_id(
                user_id).get_given_tasks():  # At least one task has been given
            return 'There are no problems meeting your criteria', "please choose a different subject and/or complexity" # Короче фиг знает,

        task = tasks[0]
        title = f'**{task.get_task_name(self)}**'
        statement = task.get_statement()
        return f'{title}\n\n{statement}', task.get_id()
