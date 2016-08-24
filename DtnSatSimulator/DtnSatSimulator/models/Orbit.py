'''
Created on 19 de ago. de 2016

@author: pabli
'''
from django.db import models
from datetime import datetime
import ephem
from DtnSatSimulator.Utils.MathUtils import AttitudeToPeriod


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
    
    #_orekitOrbit = None 
    #_propagator  = None
    epSat = None
       
    
    @classmethod
    def create(cls, eccentricity, semimajorAxis, inclination, longitudeAscendingNode, argumentPeriapsis, meanAnomaly):        
        result = cls()
        result.eccentricity             = eccentricity
        result.semimajorAxis            = semimajorAxis
        result.inclination              = inclination
        result.longitudeAscendingNode   = longitudeAscendingNode
        result.argumentPeriapsis        = argumentPeriapsis
        result.meanAnomaly              = meanAnomaly
        result.pyEpoch                  = ephem.now()
        
        
        """        
        _epoch � Reference epoch
        _n � Mean motion, in revolutions per day
        _inc � Inclination (�)
        _raan � Right Ascension of ascending node (�)
        _e � Eccentricity
        _ap � Argument of perigee at epoch (�)
        _M � Mean anomaly from perigee at epoch (�)
        
        _decay � Orbit decay rate in revolutions per day, per day
        _drag � Object drag coefficient in per earth radii
        _orbit � Integer orbit number of epoch
        """
        result.epSat        = ephem.EarthSatellite(ephem.now())
        result.epSat._n     = AttitudeToPeriod((ephem.earth_radius/1000)+semimajorAxis) #� Mean motion, in revolutions per day
        result.epSat._inc   = inclination#46.8
        result.epSat._e     = result.eccentricity#1.4538821258014423e-09
        result.epSat._ap    = argumentPeriapsis  #  0.0
        result.epSat._raan  = longitudeAscendingNode
        result.epSat._M     = meanAnomaly
        result.epSat._epoch = result.pyEpoch # '2014/02/14 13:00:00' Aparentemente es la epoca del TLE o de los elementos orbitales
        
        result._decay       = 0#— Orbit decay rate in revolutions per day, per day
        result._drag        = 0#— Object drag coefficient in per earth radii
        result._orbit       = 0#— Integer orbit number of epoch

       
        
        
        #sma = 6878.13631
        
        return result
        
    def getPosition(self, dt):
        #La cosa es que el primer parametro es el momento que se busca y el segundo la epoca del TLE o elementos orbitales
        self.epSat.compute(dt, epoch=ephem.now())
        return self.epSat.g_ra, self.epSat.sublat, self.epSat.sublong, self.epSat.elevation
        
    
    def __str__(self):
        return "Orbita, excentricidad: "+str(self.eccentricity)+", etc"

