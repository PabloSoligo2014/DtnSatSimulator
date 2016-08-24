'''
Created on 19 de ago. de 2016

@author: pabli
'''

from django.db import models
from datetime import *
import ephem

from DtnSatSimulator.models.Node import Node
from DtnSatSimulator.models.Orbit import Orbit


class Satellite(Node):
    '''
    classdocs
    '''
    noradId = models.IntegerField(null=True)
    orbit = models.ForeignKey('Orbit')
    
    
    
    
    
    #keplerian parameters: {a: 7069220.386682823; e: 4.777356060557311E-4; i: 98.18525099174988; pa: 13.741061002484528; raan: 150.34825333049; v: -13.952151446378437;}
    @classmethod
    def create(cls, eccentricity, semimajorAxis, inclination, longitudeAscendingNode, argumentPeriapsis, meanAnomaly):        
        result = cls()
        result.pyEpoch                  = datetime.utcnow()
        result.orbit = Orbit.create(eccentricity, semimajorAxis, inclination, longitudeAscendingNode, argumentPeriapsis, meanAnomaly)
        return result


    def __str__(self):
        return None
    
    def getPosition(self, dt):
        
        return self.orbit.getPosition(dt)
        
        