from task.user import User


class UsersManager:
    users = []

    def add_user(self, user: User):
        self.users.append(user)