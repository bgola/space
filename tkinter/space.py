#!/usr/bin/env python

from Tkinter import *

master = Tk()

canvas = Canvas(master, width=800, height=600, background='black')
canvas.pack()

class Grid(object):
    def __init__(self, canvas):
        self.canvas = canvas
        self.cell_width = 10
        self.cell_height = 10
        self.width = 80
        self.height = 60

    def draw(self, x, y, tags=None):
        self.canvas.create_rectangle(x * self.cell_width,
                                     y*self.cell_height,
                                     x * self.cell_width + self.cell_width,
                                     y*self.cell_height + self.cell_height, 
                                     fill="white", outline="white", tags=tags)

    def draw_object(self, x, y, obj):
        for j, line in enumerate(obj):
            for i, v in enumerate(line):
                if v:
                    self.draw(x+i, y+j, obj.tags)

class Object(object):
    def __init__(self, obj, x=None, y=None, tags=None):
        self.__obj = obj
        self.x = x
        self.y = y
        self.tags = tags
        
    def __iter__(self):
        return self.__obj.__iter__()

    def draw(self):
        canvas.draw_object(self)

grid = Grid(canvas)

spaceship = Object([[0,0,1,0,0],
                    [1,0,1,0,1],
                    [1,1,1,1,1]], tags="spaceship")


heart = Object([[0,1,0,1,0],
                [1,1,1,1,1],
                [1,1,1,1,1],
                [0,1,1,1,0],
                [0,0,1,0,0]])

bullet = [[1]]
import random
grid.draw_object(37, 55, spaceship)
for i, x in enumerate(range(10, 65, 10)):
    grid.draw_object(x, random.randint(1,10), Object([[1,0,1],
                                                      [0,1,0]], tags=("enemy%d" %i, "enemies")))
#mainloop()

