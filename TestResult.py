#-*- coding: utf-8 -*-
#__author__ = Bernardo Gomes
#27/05/2016 
#21:29


class TestResult:

    def __init__(self):
        self.runCount = 0
        self.errorCount = 0

    def testStarted(self):
        self.runCount +=1

    def testFailed(self):
        self.errorCount +=1

    def summary(self):
        return "%d run, %d failed" % (self.runCount, self.errorCount)
