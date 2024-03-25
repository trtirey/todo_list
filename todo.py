import customtkinter
from datetime import date
import json
import task

##
## To Do
##  X Finish button functionality to add a new task
##  X Implement a button to save unchecked tasks to a file
##  X Implement loading in tasks from file (or db?)
##  - Clean up saving and loading; create a seperate function for loading from file
##  - Create a github repo
##  - Implement recurring tasks
##  - implement task highlighting for overdue or completed tasks
##  - Implement button to clear tasks
##  - Implement task importance?

# Class definition for the frame that holds the checkboxes
class CheckboxFrame(customtkinter.CTkFrame):
    # When instantiating, this class takes a title and a set of values that will provide the text for the checkboxes
    def __init__(self, master, title, values):
        super().__init__(master)
        # Set the column to fill all the space it has available
        self.grid_columnconfigure(0, weight=1)
        self.title = title
        self.values = values    # values is a list of task objects
        self.checkboxes = []

        # Create the title label for the frame
        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        self.update_frame()

    # Update the checkboxes; Create the checkbox for each item in self.values; assumes each will be a task object
    def update_frame(self):
        for i, task in enumerate(self.values):
            checkbox = customtkinter.CTkCheckBox(self, text=task.title)
            checkbox.grid(row=i+1, column=0, padx=10, pady=(10,0), sticky="w")
            self.checkboxes.append(checkbox)

    # Define a get function that will return the text values of all of the currently checked boxes
    def get_checked(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get() ==1:
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes

    # Add a task to the frame
    def add_task(self, title, due=date.today()):
        self.values.append(task.task(title, due))
        self.update_frame()

# Class definition for the application; instantiating calls for a list of tasks
class App(customtkinter.CTk):
    def __init__(self, tasks):
        super().__init__()

        self.title("ToDo")
        self.geometry("350x650")
        self.grid_columnconfigure(0, weight=1)
        #self.grid_rowconfigure(1, weight=1)

        # Create the " Add Task" button; requires additional work
        self.button = customtkinter.CTkButton(self, text="Add Task", command=self.add_task_event)
        self.button.grid(row=0, column=0, padx=10, pady=20, sticky="ew")

        # Create the checkbox_frame using the CheckboxFrame defined above
        self.checkbox_frame = CheckboxFrame(self, "Tasks", values=tasks)
        self.checkbox_frame.grid(row=1, column=0, padx=10, pady=(0,20), sticky="nesw")
        self.checkbox_frame.configure(fg_color="transparent")

        # Create button to clear completed tasks
        self.button = customtkinter.CTkButton(self, text="Clear Tasks", command=self.clear_tasks_event)
        self.button.grid(row=2, column=0, padx=10, pady=(0,20), sticky="ew")

        # Create a button to save current tasks
        self.button = customtkinter.CTkButton(self, text="Save Tasks", command=self.save_tasks_event)
        self.button.grid(row=3, column=0, padx=10, pady=(0,20), sticky="ew")
        

    # Defines a function for the Add Task button
    def add_task_event(self):
        dialog = customtkinter.CTkInputDialog(text="Enter Task", title="Create Task")
        self.checkbox_frame.add_task(dialog.get_input())

    # Defines a funtion for the Clear Tasks button
    def clear_tasks_event(self):
        print("Clearing Tasks")

    # Defines a function for the Save Tasks button
    def save_tasks_event(self):
        # Create a list of dictionaries, each representing a task
        tasks = []
        for task in self.checkbox_frame.values:
            tasks.append(task.dict())
        # Write the list of task dicts to  json file
        with open("tasks.json", "w") as write_file:
            json.dump(tasks, write_file)
        #print("Saving Tasks")


##
##
##

          
def load_tasks_from_file(json_file):
    # Load tasks in from file
    tasks = []
    # Try loading tasks from file; if the file doesn't exist, create an empty list
    try:
        with open(json_file, "r") as read_file:
            # Try to load file; if the file is empty, create an empty list
            try:
                raw_tasks = json.load(read_file)
            except:
                raw_tasks = []
    except:
        raw_tasks = []
    #print(raw_tasks)
    # Create a list by parsing each dictionary as a task object
    for obj in raw_tasks:
        tasks.append(task.task(obj['Title'], date.fromisoformat(obj['Deadline'])))
    return tasks


###
###
###


if __name__ == "__main__":
    tasks = load_tasks_from_file("tasks.json")
    
    app=App(tasks)
    app.mainloop()