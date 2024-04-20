import tkinter as tk
from tkinter import ttk


class HomePage(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#A7E7F6")
        self.master = master
        # page canvas
        canvas = tk.Canvas(self, scrollregion=(0, 0, 2000, 5000),bg="#A7E7F6")
        canvas.create_text(275, 1900, text="Welcome, Stephen", fill="#225A76",
                           font=('Helvetica', 35, 'bold'))
        canvas.create_line(0,0,2000,5000,fill='green', width=10)
        canvas.pack(expand=True,fill='both')

        # scrollbar
        scrollbar = ttk.Scrollbar(self, orient='vertical', command=canvas.yview)
        scrollbar.place(relx=1, rely=1, relheight=1, anchor='ne')
        canvas.configure(yscrollcommand=scrollbar.set)
        # tk.Button(self, text="Go to [] Page", command=self.goto_weather).pack()

    def show(self):
        self.pack(fill='both', expand=True)

    def goto_(self):
        self.pack_forget()  # Hide the current page
        # self.master.weather_page.show()
