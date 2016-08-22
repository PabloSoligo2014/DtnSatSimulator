'''
Created on 19 de ago. de 2016

@author: pabli
'''
from django.db import models


class Node(models.Model):
    '''
    classdocs
    '''
    code = models.CharField('Codigo del satelite', max_length=24, help_text='Codigo del satelite, ejemplo FS2017', unique=True)
    description = models.CharField("Descripcion", max_length=120, help_text="Descripcion", blank=True)
    
    
    def __str__(self):
        return None

