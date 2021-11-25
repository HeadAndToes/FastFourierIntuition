import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt


picW = 250
picH = 250
picSpace= np.ones((picW,picH))*0



root = tk.Tk()
root.title("Paint Application")
root.geometry("500x350")



def paint(event):
    # get x1, y1, x2, y2 co-ordinates
    x1, y1 = (event.x), (event.y)
    x2, y2 = (event.x), (event.y)
    color = "black"
    # display the mouse movement inside canvas
    wn.create_oval(x1, y1, x2, y2, fill=color, outline=color)
    if (0 <= x1) and  (x1 < picW) and 0<=y1 and y1<picH:
        picSpace[x1,y2]= 255
    
# create canvas
wn=tk.Canvas(root, width=picW, height=picH, bg='white')
# bind mouse event with canvas(wn)
wn.bind('<B1-Motion>', paint)
wn.pack()
root.mainloop()

print("closed app")
plt.imshow(picSpace, cmap='gray')