'''
Created on 2013-7-4

@author: qminming
'''
import unittest
from sort import sortx
from nose.tools import *

class Test(unittest.TestCase):

    def testletters(self):
        csv = sortx(1, 2)
        n1 = csv.to_int("c")
        assert_equal(n1, 3)
        n2 = csv.to_int("ac")
        assert_equal(n2, 29)
        n3 = csv.to_int("abc")
        assert_equal(n3, 731)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()