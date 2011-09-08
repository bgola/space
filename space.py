#!/usr/bin/env python

from Tkinter import Tk, Canvas, mainloop

class Grid(object):
    cell_size = 5

    def __init__(self):
        master = Tk()
        self.canvas = Canvas(master, width=800, height=600, background='black')
        self.canvas.pack()
        self.columns = int(self.canvas['width']) / self.cell_size
        self.rows = int(self.canvas['height']) / self.cell_size

    def put(self, x, y, tags=None):
        self.canvas.create_rectangle(x * self.cell_size,
                                     y*self.cell_size,
                                     x * self.cell_size + self.cell_size,
                                     y*self.cell_size + self.cell_size, 
                                     fill="white", outline="white", tags=tags)

    def move(self, tags, dx, dy):
        self.canvas.move(tags, dx*self.cell_size, dy*self.cell_size)

class Unit(object):
    bitmap = None
    instance_count = 0

    def __init__(self, grid, x=0, y=0, tags=()):
        self.x = x
        self.y = y
        self.grid = grid
        self.tag = "%s_%d" % (self.__class__.__name__, self.__class__.instance_count)
        self.extra_tags = (self.__class__.__name__, self.tag) + tags
        self.__class__.instance_count += 1
        
    def put(self):
        for j, line in enumerate(self.bitmap):
            for i, v in enumerate(line):
                if v:
                    self.grid.put(self.x+i, self.y+j, self.extra_tags)

    def move(self, dx, dy):
        self.grid.move(self.tag, dx, dy)
