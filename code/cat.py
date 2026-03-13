#!/usr/bin/python
# -*- coding: utf-8 -*-

from Mammal import Mammal


class Cat(Mammal):
    def __init__(self, age, weight, height, length, position):
        super().__init__(age, weight, height, length, position)
        self.breed = None
        self.tail_length = None