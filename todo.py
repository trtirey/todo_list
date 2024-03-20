import customtkinter
import task

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("ToDo")
        self.geometry("350x650")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.button = customtkinter.CTkButton(self, text="Add Task", command=self.button_callback)
        self.button.grid(row=0, column=0, padx=10, pady=20, sticky="ew")

        self.checkbox_frame = customtkinter.CTkFrame(self)
        self.checkbox_frame.grid(row=1, column=0, padx=10, pady=(0,20), sticky="nsw")
        self.checkbox_1 = customtkinter.CTkCheckBox(self.checkbox_frame, text="Task 1")
        self.checkbox_1.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        self.checkbox_2 = customtkinter.CTkCheckBox(self.checkbox_frame, text="Task 2")
        self.checkbox_2.grid(row=2, column=0, padx=10, pady=10, sticky="ew")


    def button_callback(self):
        print("Button Pressed")



app=App()
app.mainloop()