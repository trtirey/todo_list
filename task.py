from datetime import date


class task:
    def __init__(self, title, day_due = date.today()):
        self.title = title
        self.deadline = day_due