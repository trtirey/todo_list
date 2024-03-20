import customtkinter
import task

##
## To Do
##  - Finish button functionality to add a new task
##  - Implement a button to save unchecked tasks to a file
##  - Implement loading in tasks from file (or db?)

# Class definition for the frame that holds the checkboxes
class CheckboxFrame(customtkinter.CTkFrame):
    # When instantiating, this class takes a title and a set of values that will provide the text for the checkboxes
    def __init__(self, master, title, values):
        super().__init__(master)
        # Set the column to fill all the space it has available
        self.grid_columnconfigure(0, weight=1)
        self.title = title
        self.values = values
        self.checkboxes = []

        # Create the title label for the frame
        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        # Create the checkbox for each item in self.values; assumes each will be a task object
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


# Class definition for the application; instantiating calls for a list of tasks
class App(customtkinter.CTk):
    def __init__(self, tasks):
        super().__init__()

        self.title("ToDo")
        self.geometry("350x650")
        self.grid_columnconfigure(0, weight=1)
        #self.grid_rowconfigure(1, weight=1)

        # Create the " Add Task" button; requires additional work
        self.button = customtkinter.CTkButton(self, text="Add Task", command=self.button_event)
        self.button.grid(row=0, column=0, padx=10, pady=20, sticky="ew")

        # Create the checkbox_frame using the CheckboxFrame defined above
        self.checkbox_frame = CheckboxFrame(self, "Tasks", values=tasks)
        self.checkbox_frame.grid(row=1, column=0, padx=10, pady=(0,20), sticky="nesw")
        self.checkbox_frame.configure(fg_color="transparent")
        

    # Defines a function for the action of the button; needs finishing
    def button_event(self):
        dialog = customtkinter.CTkInputDialog(text="Enter Task", title="Create Task")
        print(dialog.get_input())
        #return task.task(dialog.get_input())
        #print("checkbox_frame_1:", self.checkbox_frame.get_checked())


if __name__ == "__main__":
    # Create a dummy list of tasks; replace with a file read-in for task persistence
    tasks = [task.task("Eat"),
             task.task("Sleep"),
             task.task("Repeat")]
    app=App(tasks)
    app.mainloop()