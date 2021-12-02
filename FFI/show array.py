# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 13:52:23 2021

@author: tim.toenz

"""

import numpy as np
import tkinter as tk

from PIL import Image, ImageTk

root = tk.Tk()

array = np.ones((40,40))*255
img =  ImageTk.PhotoImage(image=Image.fromarray(array),master=root)

canvas = tk.Canvas(root,width=300,height=300)
canvas.pack()
canvas.create_image(20,20, anchor="nw", image=img)

root.mainloop()