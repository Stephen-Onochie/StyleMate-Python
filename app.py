# Needed libraries
import tkinter as tk
import time
from tkinter import ttk
from Services import database as db

# importing app pages
from Pages import outfits
from Pages import settings
from Pages import wardrobe
from Pages import weather
from Pages import home
from Pages import loading

# --------------APP LOOP-------------------------
# loading screen
loading.run()
time.sleep(5)

while True:
    home.run()