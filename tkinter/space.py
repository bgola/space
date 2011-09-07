#!/usr/bin/env python

from Tkinter import *

master = Tk()

canvas = Canvas(master, width=800, height=600, background='black')
canvas.pack()

class Grid(object):
    cell_size = 5

    def __init__(self, canvas):
        self.columns = int(canvas['width']) / self.cell_size
        self.rows = int(canvas['height']) / self.cell_size
        self.canvas = canvas

    def draw(self, x, y, tags=None):
        self.canvas.create_rectangle(x * self.cell_size,
                                     y*self.cell_size,
                                     x * self.cell_size + self.cell_size,
                                     y*self.cell_size + self.cell_size, 
                                     fill="white", outline="white", tags=tags)

class Unit(object):
    bitmap = None
    instance_count = 0

    def __init__(self, grid, x=0, y=0, tags=()):
        self.x = x
        self.y = y
        self.grid = grid
        self.tags = (self.__class__.__name__, self.__class__.instance_count) + tags
        self.__class__.instance_count += 1
        
    def draw(self):
        for j, line in enumerate(self.bitmap):
            for i, v in enumerate(line):
                if v:
                    self.grid.draw(self.x+i, self.y+j, self.tags)


def testcase():
    grid = Grid(canvas)

    class Spaceship(Unit):
        bitmap =((0,0,1,0,0),
                 (1,0,1,0,1),
                 (1,1,1,1,1))

    class Enemy(Unit):
        bitmap = ((1,0,1),
                  (0,1,0))

    import random
    sp = Spaceship(grid, 80, 100)
    sp.draw()
    for i, x in enumerate(range(10, 65, 5)):
        enemy = Enemy(grid, x, random.randint(1,10))
        enemy.draw()
#mainloop()
testcase()

