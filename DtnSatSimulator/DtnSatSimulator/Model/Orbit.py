'''
Created on 19 de ago. de 2016

@author: pabli
'''
from django.db import models
from datetime import datetime
import ephem


class Orbit(models.Model):
    '''
    classdocs
    '''
    
    eccentricity            = models.FloatField()
    semimajorAxis           = models.FloatField()
    inclination             = models.FloatField()
    longitudeAscendingNode  = models.FloatField()
    argumentPeriapsis       = models.FloatField()
    meanAnomaly             = models.FloatField()
    pyEpoch                 = models.DateTimeField()
    
    _orekitOrbit = None 
    _propagator  = None
       
    
    #keplerian parameters: {a: 7069220.386682823; e: 4.777356060557311E-4; i: 98.18525099174988; pa: 13.741061002484528; raan: 150.34825333049; v: -13.952151446378437;}
    @classmethod
    def create(cls, eccentricity, semimajorAxis, inclination, longitudeAscendingNode, argumentPeriapsis, meanAnomaly):        
        result = cls()
        result.eccentricity             = eccentricity
        result.semimajorAxis            = semimajorAxis
        result.inclination              = inclination
        result.longitudeAscendingNode   = longitudeAscendingNode
        result.argumentPeriapsis        = argumentPeriapsis
        result.meanAnomaly              = meanAnomaly
        result.pyEpoch                  = datetime.utcnow()
        
        
        
        
        #setup_orekit_curdir()
 
        #
        #adate = datetime_to_absolutedate(datetime.utcnow()) 
        #print adate
        #dt = absolutedate_to_datetime(adate)
        #print "Datetime ", dt
        
        #inertialFrame = FramesFactory.getEME2000()
        #self.orekitOrbit    = KeplerianOrbit(result.semimajorAxis, 
        #                                     result.eccentricity, 
        #                                     result.inclination, 
        #                                     result.argumentPeriapsis, 
        #                                     result.longitudeAscendingNode, 
        #                                     result.meanAnomaly, 
        #                                     inertialFrame, 
        #                                     datetime_to_absolutedate(datetime.utcnow()), 
        #                                     Constants.WGS84_EARTH_MU);
        #self.propagator     = KeplerianPropagator(self.orekitOrbit);
    
        
        """
        Frame inertialFrame = FramesFactory.getGCRF();
        self.orekitOrbit = new KeplerianOrbit(a, e, i, omega, raan, lM, PositionAngle.MEAN,inertialFrame, initialDate, mu);
        
        self.propagator = new KeplerianPropagator(this.orekitOrbit);
        
        self.propagator.setSlaveMode();            
        """
        return result
        
    def getPosition(self):
        pass
    
    def __str__(self):
        return "orbit!"

