import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image , ImageTk

picW = 250
picH = 250
picSpace= np.ones((picW,picH))*255



root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
root.title("Paint Application")
root.geometry("500x350")
leftFrame = tk.Frame(root)
leftFrame.pack(side= tk.LEFT)

rightFrame = tk.Frame(root)
rightFrame.pack(side = tk.RIGHT)


def paint(event):
    # get x1, y1, x2, y2 co-ordinates
    x1, y1 = (event.x), (event.y)
    x2, y2 = (event.x), (event.y)
    color = "black"
    # display the mouse movement inside canvas
    wn.create_oval(x1, y1, x2, y2, fill=color, outline=color)
    if (0 <= x1) and  (x1 < picW) and 0<=y1 and y1<picH:
        picSpace[x1,y2]= 0
    
    
    
def render(event):
    
    img =  ImageTk.PhotoImage(image=Image.fromarray(picSpace),master=root)

    canvas = tk.Canvas(rightFrame,width=250,height=250,background = 'red')
    canvas.pack()
    canvas.create_image(250,250, image=img)
    print("render called")
# create canvas



wn=tk.Canvas(leftFrame, width=picW, height=picH, bg='white')
# bind mouse event with canvas(wn)
wn.bind('<B1-Motion>', paint)
wn.bind('<ButtonRelease-1>', render)
wn.pack()




# # show image
# image1 = pil.open("SpaceImage.png")
# test = pil.ImageTk.PhotoImage(image1)

# label1 = tk.tkinter.Label(image=test)
# label1.image = test

# # Position image
# label1.place(x=100, y=100)
# root.mainloop()


root.mainloop()


im = Image.fromarray(picSpace)

if im.mode != 'RGB':
    im = im.convert('RGB')
im.save("SpaceImage.png")

print("closed app")
plt.imshow(picSpace, cmap='gray')
