'''
Created on 21 de ago. de 2016

@author: pabli
'''
import unittest

from DtnSatSimulator.Utils.MathUtils import SemiaxisToPeriod
import ephem

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testName(self):
        
        print("Earth radious", ephem.earth_radius)
        val = SemiaxisToPeriod(ephem.earth_radius+700000)
        print( val )


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()