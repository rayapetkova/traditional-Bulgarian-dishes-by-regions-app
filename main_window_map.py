import tkinter as tk
from PIL import ImageTk, Image
from base_region_class_structure import BaseRegion
from helpers import clean_widgets_from_frame
from regions_functions import *


class MainWindowMap:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Traditional Dishes")
        self.window.geometry("1300x650")
        self.window.iconphoto(False, tk.PhotoImage(file='images/bowl_of_food.png'))

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
        # self.label_image.pack()

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
                                              command=self.north_western_region)
        self.north_western_button.place(x=370, y=250)

        self.north_central_button = tk.Button(self.frame,
                                              text='North Central',
                                              font=("Constantia", 12),
                                              width=14,
                                              bd=0,
                                              bg='#aee8a7',
                                              cursor='hand2',
                                              command=self.north_central_region)
        self.north_central_button.place(x=708, y=203)

        self.north_eastern_button = tk.Button(self.frame,
                                              text='North Eastern',
                                              font=("Constantia", 12),
                                              width=14,
                                              bd=0,
                                              bg='#cceb8a',
                                              cursor='hand2',
                                              command=self.north_eastern_region)
        self.north_eastern_button.place(x=860, y=250)

        self.south_western_button = tk.Button(self.frame,
                                              text='South Western',
                                              font=("Constantia", 12),
                                              width=14,
                                              bd=0,
                                              bg='#faa5a5',
                                              cursor='hand2',
                                              command=self.south_western_region)
        self.south_western_button.place(x=270, y=425)

        self.south_central_button = tk.Button(self.frame,
                                              text='South Central',
                                              font=("Constantia", 12),
                                              width=14,
                                              bd=0,
                                              bg='#fad5a7',
                                              cursor='hand2')
        self.south_central_button.place(x=510, y=490)

        self.south_eastern_button = tk.Button(self.frame,
                                              text='South Eastern',
                                              font=("Constantia", 12),
                                              width=14,
                                              bd=0,
                                              bg='#fff799',
                                              cursor='hand2')
        self.south_eastern_button.place(x=740, y=380)

    def start_main_window(self):
        self.window.mainloop()

    def north_western_region(self):
        clean_widgets_from_frame(self.frame)

        new_frame = north_western(self.window)
        self.frame = new_frame

    def north_central_region(self):
        clean_widgets_from_frame(self.frame)

        new_frame = north_central(self.window)
        self.frame = new_frame

    def north_eastern_region(self):
        clean_widgets_from_frame(self.frame)

        new_frame = north_eastern(self.window)
        self.frame = new_frame

    def south_western_region(self):
        clean_widgets_from_frame(self.frame)

        new_frame = south_western(self.window)
        self.frame = new_frame


mainw = MainWindowMap()
mainw.start_main_window()
