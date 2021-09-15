from tkinter import *


def hello():
    print("hello")


tk = Tk()
btn = Button(tk, text="click", command=hello)
btn.pack()

btn.mainloop()
