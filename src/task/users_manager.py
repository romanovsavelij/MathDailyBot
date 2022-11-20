from task.user import User
from typing import List, Dict


class UsersManager:
    def __init__(self):
        self.users: Dict[int, User] = {}

    def add_user(self, user: User):
        self.users[user.id] = user
        # self.users.append(user)

    def erase_user(self, user: User):
        del self.users[user.id]
        # self.users.remove(user)

    def get_users(self):
        return self.users

    def get_user_by_id(self, user_id: int) -> User:
        return self.users[user_id]
