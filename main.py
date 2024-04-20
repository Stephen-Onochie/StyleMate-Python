import tkinter as tk
import time

from Pages import home
from Pages import loading
from Pages import outfits
from Pages import settings
from Pages import wardrobe
from Pages import weather


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('StyleMate - Python Demo')
        width = 350
        height = 600
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        # Init pages
        self.home_page = home.HomePage(self)

# --------------APP LOOP-------------------------
