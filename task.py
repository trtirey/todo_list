## To Do
##  - Assert a set of possible values for priority


from datetime import date


class task:
    def __init__(self, title, due = date.today(), priority="Low"):
        self.title = title
        self.deadline = due
        self.importance = priority

    def dict(self):
        obj_dict = {"Title":self.title, 
                    "Deadline":str(self.deadline),
                    "Importance":self.importance}
        return obj_dict


#def to_json:

#def from_json: