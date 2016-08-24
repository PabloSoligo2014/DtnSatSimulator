'''
Created on 19 de ago. de 2016

@author: pabli
'''
from django.db import models
from DtnSatSimulator.models.Constellation import Constellation




class Node(models.Model):
    '''
    classdocs
    '''
    code = models.CharField('Codigo del satelite', max_length=24, help_text='Codigo del satelite, ejemplo FS2017', unique=True)
    description = models.CharField("Descripcion", max_length=120, help_text="Descripcion", blank=True)
    #, through='NodeConstellation'
    constellations = models.ManyToManyField(Constellation, blank=True, null=True, related_name="nodes")

    
    def __str__(self):
        return self.code
    
    class Meta:
        ordering = ('code',)

