#!/usr/bin/env python

import unittest
import space

from space import Grid

class DumbGrid(object):
    pass

class SpaceUnitTest(unittest.TestCase):

    def setUp(self):
        self.grid = Grid()
        # resets the Unit.instance_count
        reload(space)

    def tearDown(self):
        del self.grid

    def test_unit_instance_counter(self):
        u = space.Unit(self.grid)
        self.assertEquals(space.Unit.instance_count, 1)
        for i in range(10):
            u = space.Unit(self.grid)
        self.assertEquals(space.Unit.instance_count, 11)

    def test_unit_tag(self):
        u = space.Unit(self.grid)
        self.assertEquals(u.tag, 'Unit_0')
        u2 = space.Unit(self.grid)
        self.assertEquals(u2.tag, 'Unit_1')

    def test_unit_extra_tags(self):
        u = space.Unit(self.grid)
        self.assertEquals(len(u.extra_tags), 2)
        self.assertEquals(u.extra_tags[0], 'Unit')
        self.assertEquals(u.extra_tags[1], 'Unit_0')
        u2 = space.Unit(self.grid)
        self.assertEquals(len(u2.extra_tags), 2)
        self.assertEquals(u2.extra_tags[0], 'Unit')
        self.assertEquals(u2.extra_tags[1], 'Unit_1')

    def test_unit_inheritance_instance_count(self):
        class MyUnit(space.Unit):
            bitmap = ((1,1,1),)

        self.assertEquals(MyUnit.instance_count, 0)
        mu = MyUnit(self.grid)
        self.assertEquals(MyUnit.instance_count, 1)
    
    def test_unit_inheritance_tags(self):
        class MyUnit(space.Unit):
            bitmap = ((1,1,1),)
        mu = MyUnit(self.grid)
        self.assertEquals(mu.tag, 'MyUnit_0')
        self.assertEquals(mu.extra_tags, ('MyUnit', 'MyUnit_0'))
 
    def test_unit_multiple_children(self):
        class Spaceship(space.Unit):
            bitmap = ((0,1,0),(1,1,1))

        class Monster(space.Unit):
            bitmap = ((1,0,1),(0,1,0),(1,0,1))

        spaceship = Spaceship(self.grid)
        monster_0 = Monster(self.grid)
        monster_1 = Monster(self.grid)
        monster_2 = Monster(self.grid)
        self.assertEquals(Spaceship.instance_count, 1)
        self.assertEquals(Monster.instance_count, 3)
        self.assertEquals(monster_2.tag, 'Monster_2')
        self.assertEquals(monster_0.extra_tags, ('Monster', 'Monster_0'))
 


if __name__ == "__main__":
    unittest.main()


