'''
Created on Nov 10, 2015

@author: jj1745
'''
import unittest
from assignment8 import *

class Test(unittest.TestCase):
    '''
    tests our functions that help handling user inputs in assignment8.py 
    '''
    def test_getTrials(self):
        with self.assertRaises(NonPositiveException):
            getTrials('0')
        
        with self.assertRaises(InvalidNumTrialsException):
            getTrials('[234],')
            
        self.assertEqual(555, getTrials('555'))
            
    
    def test_checkPositions(self):
        with self.assertRaises(InvalidPositionsException):
            checkPositions('[1,10,20]')
            
        self.assertEqual(True, checkPositions('[1,10,100,1000]'))
            

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()