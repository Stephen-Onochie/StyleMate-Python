import tkinter as tk


class SettingsPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master,bg="#A7E7F6")
        self.master = master
        tk.Label(self, text="StyleMate - Settings").pack(pady=10)
        # tk.Button(self, text="Go to [] Page", command=self.goto_weather).pack()

    def show(self):
        self.pack(fill='both', expand=True)

    def goto_(self):
        self.pack_forget()  # Hide the current page
        # self.master.weather_page.show()
