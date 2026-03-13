#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.animal import Animal 


class Mammal(Animal):
    def __init__(self, age, weight, height, length, position):
        super().__init__(age, weight, height, length, position)
        self.fur_type = None
        self.fur_color = None
        self.eye_color = None