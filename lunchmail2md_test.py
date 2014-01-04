#!/usr/bin/python

import unittest
import lunchmail2md

class LunchTest(unittest.TestCase):
    def testSimple(self):
        text = open('sample-2014-01-04.txt', 'r').read()
        result = lunchmail2md.main(text)
        print '------'
        print result
        print '------'

if __name__ == '__main__':
    unittest.main()