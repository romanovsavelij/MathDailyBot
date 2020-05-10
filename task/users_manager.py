from task.user import User
from typing import List


class UsersManager:
    def __init__(self):
        self.users: List[User] = []

    def add_user(self, user: User):
        self.users.append(user)

    def erase_user(self, user: User):
        self.users.remove(user)

    def get_list_of_users(self):
        return self.users

    def get_user_by_id(self, user_id: int) -> User:
        # This is copy!!!
        for user in self.users:
            if user.get_user_id() == user_id:
                return user
        print('No such a user found')

    def get_user_ind_by_id(self, user_id: int) -> int:
        for ind, user in enumerate(self.users):
            if user.get_user_id() == user_id:
                return ind
        print('No such a user found')
