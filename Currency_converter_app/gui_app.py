from tkinter import *

window = Tk()

WIDTH = 700
HEIGHT = 500
TITLE = "Currency Converter"
ICON = PhotoImage(file="Images//Money-Bag-emoji.png")

window.title(f"""{TITLE}""")
window.geometry(f"{WIDTH}x{HEIGHT}")
window.iconphoto(True, ICON)

window.mainloop()
