#-*- coding: utf-8 -*-
#__author__ = Bernardo Gomes

class TestCase:
    def __init__(self, name):
        self.name = name

    def run(self):
        method = getattr(self, self.name)
        method()