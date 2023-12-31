import tkinter as tk
from PIL import ImageTk, Image
import helpers
import regions_functions


class MainWindowMap:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Traditional Dishes")
        self.window.geometry("1300x650")
        # self.window.iconphoto(False, tk.PhotoImage(file='images/bowl_of_food_window_img.png'))

        self.frame = tk.Frame(self.window,
                              width=1300,
                              height=650,
                              bg='#fae6d4')
        self.frame.grid(row=0, column=0)

        # Open the image
        self.map_img_open = Image.open("images/map_of_regions.png")

        # Resize the image
        self.resized_map_image = self.map_img_open.resize((920, 550))

        self.map_image = ImageTk.PhotoImage(self.resized_map_image)
        self.label_image = tk.Label(self.frame, image=self.map_image)
        self.label_image.place(x=190, y=90)

        self.title_main_window_label = tk.Label(self.frame,
                                                bg='#fae6d4',
                                                text='Traditional Bulgarian Dishes By Regions',
                                                font=("Constantia", 24))
        self.title_main_window_label.place(x=370, y=10)

        self.press_button_label = tk.Label(self.frame,
                                           bg='#fae6d4',
                                           text='press any button to see what dishes the region offers',
                                           font=("Constantia", 14),
                                           fg='#fa3939')
        self.press_button_label.place(x=425, y=54)

        self.north_western_button = tk.Button(self.frame,
                                              text='North Western',
                                              font=("Constantia", 12),
                                              width=15,
                                              bd=0,
                                              bg='#bfd8ff',
                                              cursor='hand2',
                                              command=lambda: self.open_region(regions_functions.north_western))
        self.north_western_button.place(x=370, y=250)

        self.north_central_button = tk.Button(self.frame,
                                              text='North Central',
                                              font=("Constantia", 12),
                                              width=14,
                                              bd=0,
                                              bg='#aee8a7',
                                              cursor='hand2',
                                              command=lambda: self.open_region(regions_functions.north_central))
        self.north_central_button.place(x=708, y=203)

        self.north_eastern_button = tk.Button(self.frame,
                                              text='North Eastern',
                                              font=("Constantia", 12),
                                              width=14,
                                              bd=0,
                                              bg='#cceb8a',
                                              cursor='hand2',
                                              command=lambda: self.open_region(regions_functions.north_eastern))
        self.north_eastern_button.place(x=860, y=250)

        self.south_western_button = tk.Button(self.frame,
                                              text='South Western',
                                              font=("Constantia", 12),
                                              width=14,
                                              bd=0,
                                              bg='#faa5a5',
                                              cursor='hand2',
                                              command=lambda: self.open_region(regions_functions.south_western))
        self.south_western_button.place(x=270, y=425)

        self.south_central_button = tk.Button(self.frame,
                                              text='South Central',
                                              font=("Constantia", 12),
                                              width=14,
                                              bd=0,
                                              bg='#fad5a7',
                                              cursor='hand2',
                                              command=lambda: self.open_region(regions_functions.south_central))
        self.south_central_button.place(x=510, y=490)

        self.south_eastern_button = tk.Button(self.frame,
                                              text='South Eastern',
                                              font=("Constantia", 12),
                                              width=14,
                                              bd=0,
                                              bg='#fff799',
                                              cursor='hand2',
                                              command=lambda: self.open_region(regions_functions.south_eastern))
        self.south_eastern_button.place(x=740, y=380)

    def open_region(self, region_func):
        new_frame = region_func(self.window, self.frame)
        helpers.clean_widgets_from_frame(self.frame)
        self.frame = new_frame


def start_app():
    main_class = MainWindowMap()
    main_window = main_class.window
    main_window.mainloop()
