class Level:
    levels = ('easy_peasy', 'easy', 'fair', 'hard', 'insane')
    task_level = 0

    def set_level(self, lev):
        self.task_level = lev

    def get_level_name(self):
        return self.levels[self.task_level]
