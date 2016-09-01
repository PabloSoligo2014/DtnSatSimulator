'''
Created on 21 de ago. de 2016

@author: pabli
'''
import unittest

from DtnSatSimulator.Utils.MathUtils import AttitudeToPeriod
import ephem
from DtnSatSimulator.models.Satellite import Satellite
from datetime import *
from DtnSatSimulator.models import Tle

class Test(unittest.TestCase):

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testName(self):
        print("Earth radious en kms", ephem.earth_radius/1000.0)
        val = AttitudeToPeriod((ephem.earth_radius/1000)+700)
        print( "Val->", val )
        
    def testCreateAndSatellitePosition(self):
        sat2 = Satellite.new("FS2017", "FS2017", 25544)
        sat2.dtLaunch = datetime.now()
        tle = Tle()
        tle.satellite = sat2
        tle.setTle(0, 0, 0, 0, 0, 0)
        sat2.save()
        
        
        sat3 = Satellite.new("FS2019", "FS2019", 37673)
        sat3.save()

        
    """    
    def testCreateAndSatellitePosition(self):
        
        #keplerian parameters: {a: 7069220.386682823; e: 4.777356060557311E-4; i: 98.18525099174988; pa: 13.741061002484528; raan: 150.34825333049; v: -13.952151446378437;}
    
    
       
        Estacion espacial internacional
        Eccentricity:    0.0001506
        inclination:    51.6427°
        perigee height:    401 km
        apogee height:    403 km
        right ascension of ascending node:    85.0350°
        argument of perigee:    162.0483°
        revolutions per day:    15.55092441
        mean anomaly at epoch:    198.0723°
        orbit number at epoch:    1536
       
        #ephem.degrees()
        sat = Satellite()
        
        
        #sat = Satellite.create(0.01, 700, 98, 150.348, 13.74, 0.0)
        
        dt = ephem.now()
        for i in range(90):
            dt += ephem.minute * 1.0
            val = sat.getPosition(dt)
            print(val)
            #sep = ephem.separation((old_az, old_alt), (sun.az, sun.alt))
            #print("%s %s %s" % (gatech.date, sun.alt, sep))
        
        
#         print(sat.orbit)
#         for i in range(1,10):
#             val = sat.getPosition(ephem.now())
#             print(val)
#         #print("%s %s %s" % (iss.rise_time, iss.transit_time, iss.set_time)) 2003/3/23 00:00:50 2003/3/23 00:03:26 2003/3/23 00:06:01
        """

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()