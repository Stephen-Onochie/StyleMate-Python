import tkinter as tk
from tkinter import ttk


class HomePage(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#A7E7F6")
        self.master = master

        # Create a frame to contain the canvas and scrollbar
        self.frame = tk.Frame(self)
        self.frame.pack(fill='both', expand=True)

        # Create canvas
        self.canvas = tk.Canvas(self.frame, bg="#A7E7F6")
        self.canvas.pack(side='left', fill='both', expand=True)

        # Create scrollbar
        self.scrollbar = ttk.Scrollbar(self.frame, orient='vertical', command=self.canvas.yview)
        self.scrollbar.pack(side='right', fill='y')

        # Configure canvas
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>', self.on_canvas_configure)

        # Add content to the canvas
        self.canvas.create_text(275, 1900, text="Welcome, Stephen", fill="#225A76",
                                font=('Helvetica', 35, 'bold'))
        self.canvas.create_line(0, 0, 2000, 5000, fill='green', width=10)

    def on_canvas_configure(self, event):
        # Set the scroll region to encompass the canvas
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))

    def show(self):
        self.pack(fill='both', expand=True)

    def goto_(self):
        self.pack_forget()  # Hide the current page
        # self.master.weather_page.show()


if __name__ == "__main__":
    root = tk.Tk()
    home_page = HomePage(root)
    home_page.show()
    root.mainloop()
