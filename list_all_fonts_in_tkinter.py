import tkinter as tk
from tkinter import font


'''SEE THE LIST OF AVAILABLE FONTS IN TKINTER'''
def preview_fonts():
    root = tk.Tk()
    root.title("Font Styles Preview")

    # Get the list of available fonts
    available_fonts = font.families()

    # Create a text widget to display the font styles
    text_widget = tk.Text(root, width=50, height=20, font=("Arial", 12))
    text_widget.pack()

    # Display each font style in the text widget
    for font_style in available_fonts:
        text_widget.insert(tk.END, font_style + "\n")

    root.mainloop()


# Call the function to preview fonts
preview_fonts()
