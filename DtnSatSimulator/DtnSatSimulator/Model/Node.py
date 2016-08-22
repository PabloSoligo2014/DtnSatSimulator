'''
Created on 19 de ago. de 2016

@author: pabli
'''
from django.db import models


class Node(models.Model):
    '''
    classdocs
    '''
    code = models.CharField("Nodo", max_length=30, "Nodo", blank=True)
    description = models.CharField("Descripcion", max_length=120, "Descripcion", blank=True)
    
    
    def __str__(self):
        return None

