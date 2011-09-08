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
                                     fill="white", outline="white", tags=tags)a

    def move(self, tags, dx, dy):
        self.canvas.move(tags, dx*self.cell_size, dy*self.cell_size)

class Unit(object):
    bitmap = None
    instance_count = 0

    def __init__(self, grid, x=0, y=0, tags=()):
        self.x = x
        self.y = y
        self.grid = grid
        self.tag = "%s_%d" % (self.__class_name__, self.__class__.instance_count)
        self.extra_tags = (self.__class__.__name__, self.tag) + tags
        self.__class__.instance_count += 1
        
    def put(self):
        for j, line in enumerate(self.bitmap):
            for i, v in enumerate(line):
                if v:
                    self.grid.put(self.x+i, self.y+j, self.extra_tags)

    def move(self, dx, dy):
        self.grid.move(self.tag, dx, dy)

testcase = True
if testcase:
    grid = Grid()

    class Spaceship(Unit):
        bitmap =((0,0,1,0,0),
                 (1,0,1,0,1),
                 (1,1,1,1,1))

    class Enemy(Unit):
        bitmap = ((1,0,1),
                  (0,1,0))

    import random
    sp = Spaceship(grid, 80, 100)
    sp.put()
    for i, x in enumerate(range(10, 65, 5)):
        enemy = Enemy(grid, x, random.randint(1,10))
        enemy.put()

