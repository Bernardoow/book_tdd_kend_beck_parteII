#-*- coding: utf-8 -*-
#__author__ = Bernardo Gomes
#27/05/2016 
#21:53

from TestResult import TestResult

class TestSuite:
    def __init__(self):
        self.tests = []

    def add(self, test):
        self.tests.append(test)

    def run(self, result):
        for test in self.tests:
            test.run(result)
        return result