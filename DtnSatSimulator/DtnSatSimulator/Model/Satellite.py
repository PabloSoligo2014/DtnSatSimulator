'''
Created on 19 de ago. de 2016

@author: pabli
'''
from DtnSatSimulator.Model.Node import Node
from django.db import models
import datetime
import ephem

class Satellite(Node):
    '''
    classdocs
    '''
    noradId = models.IntegerField(null=True)
     
    eccentricity            = models.FloatField()
    semimajorAxis           = models.FloatField()
    inclination             = models.FloatField()
    longitudeAscendingNode  = models.FloatField()
    argumentPeriapsis       = models.FloatField()
    meanAnomaly             = models.FloatField()
    pyEpoch                 = models.DateTimeField()
    
    epSat = None
    
    
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
        result.epSat                    = ephem.EarthSatellite()
        
        """        
        _epoch — Reference epoch
        _n — Mean motion, in revolutions per day
        _inc — Inclination (°)
        _raan — Right Ascension of ascending node (°)
        _e — Eccentricity
        _ap — Argument of perigee at epoch (°)
        _M — Mean anomaly from perigee at epoch (°)
        
        _decay — Orbit decay rate in revolutions per day, per day
        _drag — Object drag coefficient in per earth radii
        _orbit — Integer orbit number of epoch
        """
        
        result.epSat._n     =  #— Mean motion, in revolutions per day
        result.epSat._inc   = inclination#46.8
        result.epSat._e     = result.eccentricity#1.4538821258014423e-09
        result.epSat._ap    = argumentPeriapsis  #  0.0
        result.epSat._raan  = longitudeAscendingNode
        result.epSat._M     = meanAnomaly
        
        
        
        result.epSat._epoch = result.pyEpoch # '2014/02/14 13:00:00'
        
        result.epSat._M = #136.92
        result.epSat._raan = result.longitudeAscendingNode#199.662
        sma = 6878.13631
        result.epSat._n = #86400  * np.sqrt(398600.4418/sma**3) / (2*np.pi)
        


    def __str__(self):
        return None

        