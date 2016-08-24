'''
Created on 19 de ago. de 2016

@author: pabli
'''

from django.db import models
#from DtnSatSimulator.Model import Node

class Constellation(models.Model):
    '''
    classdocs
    '''
    
    name = models.CharField('Nombre de la constelacion', max_length=100, help_text='Nombre de la constelacion, ejemplo Iridium', unique=True)
    #nodes = models.ManyToManyField(Node, 'constellations')

    def __str__(self):
        return self.name
