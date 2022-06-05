import tkinter as tk
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(1)


def convert_temp():
    if lbl_left["text"] == "\N{DEGREE FAHRENHEIT}":
        temp_f = ent_temp.get()
        temp_c = (float(temp_f) - 32) * 5 / 9
        lbl_temp["text"] = f"{round(temp_c, 2)}"
    else:
        temp_c = ent_temp.get()
        temp_f = (float(temp_c) * 9 / 5) + 32
        lbl_temp["text"] = f"{round(temp_f, 2)}"


def reverse():
    if lbl_left["text"] == "\N{DEGREE FAHRENHEIT}":
        lbl_left["text"] = "\N{DEGREE CELSIUS}"
        lbl_right["text"] = "\N{DEGREE FAHRENHEIT}"
    else:
        lbl_left["text"] = "\N{DEGREE FAHRENHEIT}"
        lbl_right["text"] = "\N{DEGREE CELSIUS}"


window = tk.Tk()
window.title("Temperature Converter")

ent_temp = tk.Entry(master=window)
ent_temp.grid(row=0, column=0, columnspan=2)
ent_temp.insert(0, "0")


lbl_left = tk.Label(text="\N{DEGREE FAHRENHEIT}", width=5)
lbl_left.grid(row=0, column=0)

btn = tk.Button(text="\N{RIGHTWARDS BLACK ARROW}", command=convert_temp)
btn.grid(row=2, column=3)

lbl_temp = tk.Label(text="", width=10)
lbl_temp.grid(row=0, column=0)

lbl_right = tk.Label(text="\N{DEGREE CELSIUS}")
lbl_right.grid(row=0, column=3)

btn_reverse = tk.Button(
    text="\N{CLOCKWISE RIGHTWARDS AND LEFTWARDS OPEN CIRCLE ARROWS}", command=reverse
)
btn_reverse.grid(row=1, column=1)

window.mainloop()
