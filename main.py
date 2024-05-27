# pip install tk
# pip install pillow
import tkinter as tk

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
        self.setup_window()

        # Initialize pages
        self.setup_pages()

        # Show loading page and then switch to home page
        self.show_loading_page()

    def setup_window(self):
        width = 571
        height = 979
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

    def setup_pages(self):
        self.home_page = home.HomePage(self)
        self.loading_page = loading.LoadingPage(self)
        self.outfits_page = outfits.OutfitsPage(self)
        self.settings_page = settings.SettingsPage(self)
        self.wardrobe_page = wardrobe.WardrobePage(self)
        self.weather_page = weather.WeatherPage(self)

    def show_loading_page(self):
        self.loading_page.show()
        # After 3000 milliseconds (3 seconds), call self.show_home_page
        self.after(3000, self.show_home_page)

    def show_home_page(self):
        self.loading_page.close()
        self.home_page.show()


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
