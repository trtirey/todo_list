import customtkinter
import task

class CheckboxFrame(customtkinter.CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.title = title
        self.values = values
        self.checkboxes = []

        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        for i, value in enumerate(self.values):
            checkbox = customtkinter.CTkCheckBox(self, text=value)
            checkbox.grid(row=i+1, column=0, padx=10, pady=(10,0), sticky="w")
            self.checkboxes.append(checkbox)

    def get(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get() ==1:
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("ToDo")
        self.geometry("350x650")
        self.grid_columnconfigure(0, weight=1)
        #self.grid_rowconfigure(1, weight=1)

        self.button = customtkinter.CTkButton(self, text="Add Task", command=self.button_callback)
        self.button.grid(row=0, column=0, padx=10, pady=20, sticky="ew")

        self.checkbox_frame = CheckboxFrame(self, "Tasks", values=['Task 1', 'Task 2', 'Task 3', 'Task 4'])
        self.checkbox_frame.grid(row=1, column=0, padx=10, pady=(0,20), sticky="nesw")
        self.checkbox_frame.configure(fg_color="transparent")
        


    def button_callback(self):
        print(self.checkbox_frame.get())


if __name__ == "__main__":
    app=App()
    app.mainloop()