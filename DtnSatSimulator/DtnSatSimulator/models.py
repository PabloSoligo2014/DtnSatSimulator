'''
Created on Aug 22, 2016

@author: ubuntumate
'''

from DtnSatSimulator.models.Node import Node
from DtnSatSimulator.models.Orbit import Orbit
from DtnSatSimulator.models.Satellite import Satellite
from DtnSatSimulator.models.Constellation import Constellation
from DtnSatSimulator.models.GroundStation import GroundStation
from DtnSatSimulator.models.Message import Message
from DtnSatSimulator.models.Simulation import Simulation
from DtnSatSimulator.models.Track import Track
from DtnSatSimulator.models.Hope import Hope

"""
class Constellation(models.Model):
    '''
    classdocs
    '''
    
    name = models.CharField('Nombre de la constelacion', max_length=100, help_text='Nombre de la constelacion, ejemplo Iridium', unique=True)
    #nodes = models.ManyToManyField(Node, 'constellations')

    def __str__(self):
        return self.name

"""
