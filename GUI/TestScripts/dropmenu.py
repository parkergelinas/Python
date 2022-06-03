from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Parker")
root.geometry("400x400")

# Dropdown Boxes


def show():
    myLabel = Label(root, text=clicked.get()).pack()


options = ["Box #1", "Box #2", "Box #3", "Box #4"]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options)
drop.pack()

myButton = Button(root, text="Show Selection", command=show).pack()

root.mainloop()
