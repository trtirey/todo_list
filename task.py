from datetime import date


class task:
    def __init__(self, title, due = date.today()):
        self.title = title
        self.deadline = due


#def to_json:

#def from_json: