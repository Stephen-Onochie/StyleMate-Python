from PIL import Image, ImageTk
import tkinter as tk


class LoadingPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.load_background()

    def load_background(self):
        # Load and display the background image
        bg_image = Image.open('Assets/Screen_Images/StyleMate_Loading_Background.png')  # Adjust the path to your image
        bg_photo = ImageTk.PhotoImage(bg_image)

        # Make sure the canvas size matches the image size exactly
        self.canvas = tk.Canvas(self, width=bg_photo.width(), height=bg_photo.height())
        self.canvas.pack(fill="both", expand=True)

        self.canvas.create_image(0, 0, image=bg_photo, anchor="nw", tags="bg_img")

        # Keep a reference to avoid garbage collection
        self.bg_photo = bg_photo

        # Create a text item
        self.loading_text = self.canvas.create_text(275, 700, text="Loading", fill="#225A76",
                                                    font=('Helvetica', 35, 'bold'))

    def animate_loading(self):
        # Get the current text
        current_text = self.canvas.itemcget(self.loading_text, "text")

        # Update the text to simulate animation
        if current_text.endswith("..."):
            self.canvas.itemconfig(self.loading_text, text="Loading")
        else:
            self.canvas.itemconfig(self.loading_text, text=current_text + ".")

        # Schedule this method to be called again after 500ms
        self.after(500, self.animate_loading)

    def show(self):
        self.pack(fill="both", expand=True)
        self.animate_loading()  # Start the animation

    def close(self):
        self.pack_forget()
