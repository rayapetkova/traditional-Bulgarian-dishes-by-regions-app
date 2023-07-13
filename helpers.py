def clean_widgets_from_frame(c_frame):
    for widgets in c_frame.winfo_children():
        widgets.destroy()
