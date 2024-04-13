import tkinter as tk
from PIL import Image, ImageTk
import tkinter.font as tkFont

# variables
root = tk.Tk()
root.title("undefined")

# setting window size
width = 400
height = 700
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)

# Load and display an image
# (replace 'your_logo.png' with the path to your image file)
image = Image.open(r'/Users/stepheno/Documents/GitHub/StyleMate-Python/Assets/Screen_Images/StyleMate_Loading_Background.png')
image = ImageTk.PhotoImage(image)

# Create a label to display the image
image_label = tk.Label(root, image=image)
image_label.pack()


def run():
    root.mainloop()


if __name__ == "__main__":
    run()
