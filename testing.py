import datetime
import tkinter
from tkinter import *

root = tkinter.Tk()
root.title("test")
root.geometry("1000x700")

canvas = Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
canvas.pack()

bg_image = PhotoImage(file="left_arrow.png")
x = canvas.winfo_width() / 2
y = canvas.winfo_height() / 2
print(x,y)
canvas.create_image(x , y , image=bg_image)

root.mainloop()


