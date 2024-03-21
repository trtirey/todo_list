from datetime import date


class task:
    def __init__(self, title, due = date.today()):
        self.title = title
        self.deadline = due

    def dict(self):
        obj_dict = {"Title":self.title, 
                    "Deadline":str(self.deadline)}
        return obj_dict


#def to_json:

#def from_json: