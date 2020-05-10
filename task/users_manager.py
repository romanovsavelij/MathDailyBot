from task.user import User
from typing import List


# List of users
class UsersManager:
    def __init__(self):
        self.users = List[User]

    def add_user(self, user: User):
        self.users.append(user)

    def erase_user(self, user: User):
        self.users.remove(user)

    def get_list_of_users(self):
        return self.users

    def user_by_id(self, user_id: int):
        user_id_list = [user.get_user_id() for user in self.users]
        index = user_id_list.index(self, user_id)
        return self.users[index]  # reference

    def get_user(self, index):
        return self.users[index]