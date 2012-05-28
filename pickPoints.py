#!/usr/bin/python

from Tkinter import *
from Geometry import *

"""
Here I will combine tools from drawdraw to make a wee program that
will draw dots where ever the mouse is clicked on the canvas.

I will add a second feature that will draw a circle through three points 
after the third point is clicked.
"""

# for now, we will just draw points when clicked.

count = 0
point_list = {}

def makeDot(event):
    global count, point_list

    x = event.x - (canvas.winfo_width()/2)
    y = (canvas.winfo_height()/2) - event.y

    if count == 0:
        Point(x,y).draw(canvas, "red")
    elif count == 1:
        Point(x,y).draw(canvas, "green")
    else:
        Point(x,y).draw(canvas, "blue")
    
    count += 1
    point_list[count] = Point(x,y)

    if count == 3:
        threePointCircle(point_list[1], point_list[2], point_list[3]).draw(canvas)
        count = 0

root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.title(string="3-Point Circles")

canvas = Canvas(root)
canvas.grid(column=0, row=0, sticky=(N, W, E, S))
canvas.bind("<Button-1>", makeDot)

root.mainloop()    
