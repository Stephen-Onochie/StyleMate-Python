import tkinter as tk
from PIL import Image, ImageTk
import tkinter.font as tkFont

# # variables
# root = tk.Tk()
# root.title("undefined")
#
# # setting window size
# width = 350
# height = 600
# screenwidth = root.winfo_screenwidth()
# screenheight = root.winfo_screenheight()
# alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
# root.geometry(alignstr)
# root.resizable(width=False, height=False)
#
# # Load and display an image
# # (replace 'your_logo.png' with the path to your image file)
# image = Image.open(r'F:\steph\Documents\Github\StyleMate-Python\Assets\Screen_Images\StyleMate_Loading_Background.png')
# image = ImageTk.PhotoImage(image)
#
# # Create a label to display the image
# image_label = tk.Label(root, image=image)
# image_label.pack()


class LoadingPage(tk.Frame):
    def __init__(self, master):
        super().__init__(self, master)
        self.master = master
        tk.Label(self, text="App Loading").pack(pady=100)

    def show(self):
        self.pack(fill="both", expand=True)


if __name__ == "__main__":
    pass
