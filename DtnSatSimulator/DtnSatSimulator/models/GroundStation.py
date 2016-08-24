'''
Created on 19 de ago. de 2016

@author: pabli
'''
from DtnSatSimulator.models.Node import Node 
from django.db import models

class GroundStation(Node):
    '''
    classdocs
    '''
    
    latitude    = models.FloatField()
    longitude   = models.FloatField()
    altitude    = models.FloatField()
    
    def __str__(self):
        return None

