import customtkinter as ctki

app = ctki.CTk()
app.title("To Do")
app.geometry("400x650")

check = ctki.CTkCheckBox(app, text="checkbox 1")
check.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")

app.mainloop()