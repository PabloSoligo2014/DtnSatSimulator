'''
Created on 22 de ago. de 2016

@author: pabli
'''


from django.db import models
from DtnSatSimulator.models.Node import Node

class Message(models.Model):
    
    origin      = models.ForeignKey(Node)
    destination = models.ForeignKey(Node)
    
    
    
    def getActiveTrack(self):
        #El ultimo track es el activo
        #return self.tracks[0]
        return None
    
    
    
    

        