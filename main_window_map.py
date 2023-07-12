import tkinter as tk
from PIL import ImageTk, Image


class MainWindowMap:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Traditional Dishes")
        self.window.geometry("1300x650")
        self.window['background'] = '#fae6d4'
        self.window.iconphoto(False, tk.PhotoImage(file='images/bowl_of_food.png'))

        self.frame = tk.Frame(width=1500, height=500)

        # Open the image
        self.map_img_open = Image.open("images/map_of_regions.png")

        # Resize the image
        self.resized_map_image = self.map_img_open.resize((920, 550))

        self.map_image = ImageTk.PhotoImage(self.resized_map_image)
        self.label_image = tk.Label(self.window, image=self.map_image)
        self.label_image.place(x=190, y=90)
        # self.label_image.pack()

        self.title_main_window_label = tk.Label(self.window,
                                                bg='#fae6d4',
                                                text='Traditional Bulgarian Dishes By Regions',
                                                font=("Constantia", 24))
        self.title_main_window_label.place(x=370, y=10)

        self.press_button_label = tk.Label(self.window,
                                           bg='#fae6d4',
                                           text='press any button to see what dishes the region offers',
                                           font=("Constantia", 14),
                                           fg='#fa3939')
        self.press_button_label.place(x=425, y=54)

        self.north_western_button = tk.Button(self.window,
                                              text='North Western',
                                              font=("Constantia", 12),
                                              width=15,
                                              bd=0,
                                              bg='#bfd8ff',
                                              cursor='hand2')
        self.north_western_button.place(x=370, y=250)

        self.north_central_button = tk.Button(self.window,
                                              text='North Central',
                                              font=("Constantia", 12),
                                              width=14,
                                              bd=0,
                                              bg='#aee8a7',
                                              cursor='hand2')
        self.north_central_button.place(x=708, y=203)

        self.north_eastern_button = tk.Button(self.window,
                                              text='North Eastern',
                                              font=("Constantia", 12),
                                              width=14,
                                              bd=0,
                                              bg='#cceb8a',
                                              cursor='hand2')
        self.north_eastern_button.place(x=860, y=250)

        self.south_western_button = tk.Button(self.window,
                                              text='South Western',
                                              font=("Constantia", 12),
                                              width=14,
                                              bd=0,
                                              bg='#faa5a5',
                                              cursor='hand2')
        self.south_western_button.place(x=270, y=425)

        self.south_central_button = tk.Button(self.window,
                                              text='South Central',
                                              font=("Constantia", 12),
                                              width=14,
                                              bd=0,
                                              bg='#fad5a7',
                                              cursor='hand2')
        self.south_central_button.place(x=510, y=490)

        self.south_eastern_button = tk.Button(self.window,
                                              text='South Eastern',
                                              font=("Constantia", 12),
                                              width=14,
                                              bd=0,
                                              bg='#fff799',
                                              cursor='hand2')
        self.south_eastern_button.place(x=740, y=380)

    def start_main_window(self):
        self.window.mainloop()


mainw = MainWindowMap()
mainw.start_main_window()
