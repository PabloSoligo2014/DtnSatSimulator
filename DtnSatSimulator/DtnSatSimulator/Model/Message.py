'''
Created on 22 de ago. de 2016

@author: pabli
'''


from django.db import models
from DtnSatSimulator.Model import Node

class Message(models.Model):
    
    origin      = models.ForeignKey(Node)
    destination = models.ForeignKey(Node)
    
    
    
    

        