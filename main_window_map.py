import tkinter as tk
from PIL import ImageTk, Image


class MainWindowMap:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Traditional Dishes")
        self.window.geometry("1300x650")
        self.window['background'] = '#fae6d4'

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

    def start_main_window(self):
        self.window.mainloop()


mainw = MainWindowMap()
mainw.start_main_window()
