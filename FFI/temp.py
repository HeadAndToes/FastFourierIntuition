#from tkinter import *
import tkinter as tk

from PIL import ImageTk, Image
#from tkinter import filedialog
import os

root = tk.Tk()
root.geometry("550x300+300+150")
root.resizable(width=True, height=True)

def openfn():
    filename = tk.filedialog.askopenfilename(title='open')
    return filename
def open_img():
    x = openfn()
    img = Image.open(x)
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = tk.Label(root, image=img)
    panel.image = img
    panel.pack()

btn = tk.Button(root, text='open image', command=open_img).pack()

root.mainloop()