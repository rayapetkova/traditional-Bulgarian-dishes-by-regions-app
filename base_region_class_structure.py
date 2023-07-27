import tkinter as tk
from PIL import ImageTk, Image


class BaseRegion:
    def __init__(self, window, title, region, dish1, title_dish1, desc_dish1, d1_t_x, d1_t_y, d1_b_x, d1_b_y, dish2,
                 title_dish2, desc_dish2, d2_t_x, d2_t_y, d2_b_x, d2_b_y, dish3, title_dish3, desc_dish3, d3_t_x, d3_t_y,
                 d3_b_x, d3_b_y):

        self.frame = tk.Canvas(window,
                               width=1300,
                               height=650,
                               bg='#fae6d4')
        self.frame.grid(row=0, column=0)
        self.title = tk.Label(self.frame,
                              bg='#fae6d4',
                              fg='#665a51',
                              text=f'{title}',
                              font=("Constantia", 24, 'bold'))
        self.title.place(x=480, y=28)

        # Open the image
        self.first_img = Image.open(f"images/{region}/{dish1}.png")

        # Resize the image
        self.resized_first_img = self.first_img.resize((300, 200))

        self.first_img = ImageTk.PhotoImage(self.resized_first_img)
        self.label_image = tk.Label(self.frame, image=self.first_img)
        self.label_image.place(x=120, y=100)

        self.first_title = tk.Label(self.frame,
                                    bg='#fae6d4',
                                    text=f'{title_dish1}',
                                    font=("Constantia", 20, 'bold'))
        self.first_title.place(x=d1_t_x, y=d1_t_y)

        self.first_description = tk.Label(self.frame,
                                          bg='#fae6d4',
                                          text=f'{desc_dish1}',
                                          font=("Constantia", 14),
                                          width=27,
                                          height=5)
        self.first_description.place(x=115, y=365)
        self.recipe_button().place(x=d1_b_x, y=d1_b_y)

        # Open the image
        self.second_img = Image.open(f"images/{region}/{dish2}.png")

        # Resize the image
        self.resized_second_img = self.second_img.resize((300, 200))

        self.second_img = ImageTk.PhotoImage(self.resized_second_img)
        self.label_image = tk.Label(self.frame, image=self.second_img)
        self.label_image.place(x=500, y=100)

        self.second_title = tk.Label(self.frame,
                                     bg='#fae6d4',
                                     text=f'{title_dish2}',
                                     font=("Constantia", 20, 'bold'))
        self.second_title.place(x=d2_t_x, y=d2_t_y)

        self.second_description = tk.Label(self.frame,
                                           bg='#fae6d4',
                                           text=f'{desc_dish2}',
                                           font=("Constantia", 14),
                                           width=27,
                                           height=5)
        self.second_description.place(x=500, y=365)
        self.recipe_button().place(x=d2_b_x, y=d2_b_y)

        # Open the image
        self.third_img = Image.open(f"images/{region}/{dish3}.png")

        # Resize the image
        self.resized_third_img = self.third_img.resize((300, 200))

        self.third_img = ImageTk.PhotoImage(self.resized_third_img)
        self.label_image = tk.Label(self.frame, image=self.third_img)
        self.label_image.place(x=880, y=100)

        self.third_title = tk.Label(self.frame,
                                    bg='#fae6d4',
                                    text=f'{title_dish3}',
                                    font=("Constantia", 20, 'bold'))
        self.third_title.place(x=d3_t_x, y=d3_t_y)

        self.third_description = tk.Label(self.frame,
                                          bg='#fae6d4',
                                          text=f"{desc_dish3}",
                                          font=("Constantia", 14),
                                          width=27,
                                          height=5)
        self.third_description.place(x=882, y=365)
        self.recipe_button().place(x=d3_b_x, y=d3_b_y)

        self.back_button = tk.Button(self.frame,
                                     text='Back',
                                     bg='#e3d2c3',
                                     font=("Constantia", 12),
                                     width=20,
                                     height=2,
                                     bd=1,
                                     cursor='hand2')
        self.back_button.place(x=556, y=565)

    def recipe_button(self):
        recipe_button = tk.Button(self.frame,
                                  text='Recipe',
                                  font=("Constantia", 12),
                                  width=17,
                                  bd=0,
                                  bg='#e3d2c3',
                                  cursor='hand2')

        return recipe_button
