import Level
import uuid


class Task:
    # Topic (in further updates)

    # Basic
    statement_text = ""
    solution_text = ""

    # Complexity
    level = Level.Level

    # Hints
    f_hint = ""
    s_hint = ""
    hint_count = 0  # 0, 1 or 2 depending on how many hints the user has
    # asked for

    # Rating
    num_ratings = 0  # number of users who have rated the problem
    rating = 0.0

    def __init__(self, statement_text, solution_text, lev, f_hint, s_hint, rating, num_ratings):
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

    # Rating
    def get_rating(self):
        return self.rating

    def rate(self, new_rating):
        self.rating = (self.rating * self.num_ratings + new_rating) / \
                      (self.num_ratings + 1)
        self.num_ratings += 1

    # Hints
    def ask_for_hint(self):
        if not self.hint_count:
            self.hint_count += 1
            return self.f_hint
        if self.hint_count == 1:
            self.hint_count += 1
            return self.s_hint
        else:
            raise Exception("No more hints")

            '''return ("This was the last hint. You can see the solution, "
                    "but we recommend that you spend enough time "
                    "on the problem before doing so") ''' # Этот месседж можно засунуть в метод бота

    # Levels
    def set_level(self, lev):
        self.level.set_level(lev)

    def get_level_name(self):
        return self.level.get_level_name()

    
