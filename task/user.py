class User:
    solved_task_ids: str = []

    def __init__(self, user_id):
        self.id = user_id

    def solved_task(self, task_id: str):
        self.solved_task_ids.append(task_id)

    def is_solved(self, task_id: str) -> True:
        return False
