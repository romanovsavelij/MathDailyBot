from task.level import Level
from task.database import Database
import uuid


class Task:
    # Subject
    Subject = ''

    # Basic
    statement = ''
    solution = ''

    # Complexity
    level = Level()

    # Hints
    hint = ''
    is_hint = False  # True if user has asked for a hint

    # Rating (in further updates)
    # num_ratings = 0  # number of users who have rated the problem
    # rating = 0.0

    def __init__(self, statement_text, solution_text, lev, f_hint,
                 s_hint='', rating=0.0, num_ratings=0):
        self.id = uuid.uuid1()

        self.level.set_level(lev)

        self.statement_text = statement_text
        self.solution_text = solution_text

        self.level = lev

        self.f_hint = f_hint
        self.s_hint = s_hint
        self.hint_count = 0

        self.num_ratings = rating
        self.rating = num_ratings

    # Basic
    def get_statement(self):
        return self.statement_text

    def get_solution(self):
        return self.solution_text

    # Hints
    def ask_for_hint(self):
        if not self.is_hint:
            self.hint_count += 1
            return self.f_hint
        else:
            raise Exception("No more hints")

    # Levels
    def set_level(self, lev):
        self.level.set_level(lev)

    def get_level_name(self):
        return self.level.get_level_name()

    def get_id(self):
        return self.id

    def get_name(self):
        # returns task name
        return 'task name'

