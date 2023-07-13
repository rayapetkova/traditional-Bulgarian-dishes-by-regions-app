import tkinter as tk
from PIL import ImageTk, Image


class NorthWesternFrame:
    def __init__(self, window):
        self.frame = tk.Frame(window,
                              width=1300,
                              height=650,
                              bg='#fae6d4')
        self.frame.grid(row=0, column=0)

        self.title = tk.Label(self.frame,
                              bg='#fae6d4',
                              text='North Western Region',
                              font=("Constantia", 24))
        self.title.place(x=490, y=28)

        # Open the image
        self.lyutika_img = Image.open("images/north_western_region/lyutika.png")

        # Resize the image
        self.resized_lyutika_image = self.lyutika_img.resize((300, 200))

        self.lyutika_img = ImageTk.PhotoImage(self.resized_lyutika_image)
        self.label_image = tk.Label(self.frame, image=self.lyutika_img)
        self.label_image.place(x=120, y=100)

        self.lyutika_title = tk.Label(self.frame,
                                      bg='#fae6d4',
                                      text='Lyutika',
                                      font=("Constantia", 20, 'bold'))
        self.lyutika_title.place(x=228, y=320)

        self.lyutika_description = tk.Label(self.frame,
                                            bg='#fae6d4',
                                            text='Traditional vegetable mixture - \n'
                                                 'salad or chunky relish, popular in \nthe northern part of Bulgaria.'
                                                 ' \nIt is consumed in the summer.',
                                            font=("Constantia", 14),
                                            width=27,
                                            height=5)
        self.lyutika_description.place(x=115, y=365)
        self.recipe_button().place(x=200, y=495)

        # Open the image
        self.turlashka_banitsa_img = Image.open("images/north_western_region/turlashka_banitsa.png")

        # Resize the image
        self.resized_turlashka_banitsa_image = self.turlashka_banitsa_img.resize((300, 200))

        self.turlashka_banitsa_img = ImageTk.PhotoImage(self.resized_turlashka_banitsa_image)
        self.label_image = tk.Label(self.frame, image=self.turlashka_banitsa_img)
        self.label_image.place(x=500, y=100)

        self.turlashka_banitsa_title = tk.Label(self.frame,
                                                bg='#fae6d4',
                                                text='Turlashka Banitsa',
                                                font=("Constantia", 20, 'bold'))
        self.turlashka_banitsa_title.place(x=534, y=320)

        self.turlashka_banitsa_description = tk.Label(self.frame,
                                                      bg='#fae6d4',
                                                      text='One of the most iconic dishes of the \nregion.'
                                                           'The dough is divided and \nrolled '
                                                           'out into squares to be baked \non the top '
                                                           'of a wood-burning stove.',
                                                      font=("Constantia", 14),
                                                      width=27,
                                                      height=5)
        self.turlashka_banitsa_description.place(x=500, y=365)
        self.recipe_button().place(x=573, y=495)

        # Open the image
        self.kosachko_kiselo_img = Image.open("images/north_western_region/kosachko_kiselo.png")

        # Resize the image
        self.resized_kosachko_kiselo_image = self.kosachko_kiselo_img.resize((300, 200))

        self.kosachko_kiselo_img = ImageTk.PhotoImage(self.resized_kosachko_kiselo_image)
        self.label_image = tk.Label(self.frame, image=self.kosachko_kiselo_img)
        self.label_image.place(x=880, y=100)

        self.kosachko_kiselo_title = tk.Label(self.frame,
                                              bg='#fae6d4',
                                              text='Kosachko Kiselo',
                                              font=("Constantia", 20, 'bold'))
        self.kosachko_kiselo_title.place(x=928, y=320)

        self.kosachko_kiselo_description = tk.Label(self.frame,
                                                    bg='#fae6d4',
                                                    text='A cold and refreshing soup that is \n'
                                                         'traditionally prepared only \n'
                                                         'in Torlashko and only in summer.',
                                                    font=("Constantia", 14),
                                                    width=27,
                                                    height=4)
        self.kosachko_kiselo_description.place(x=882, y=365)
        self.recipe_button().place(x=962, y=495)

    def recipe_button(self):
        recipe_button = tk.Button(self.frame,
                                  text='Recipe',
                                  font=("Constantia", 12),
                                  width=17,
                                  bd=0,
                                  bg='#e3d2c3',
                                  cursor='hand2')
        return recipe_button
