'''
Created on 22 de ago. de 2016

@author: pabli
'''


from django.db import models
from DtnSatSimulator.models.Node import Node

class Message(models.Model):
    
    source      = models.ForeignKey(Node, related_name='sourceMessages')
    destination = models.ForeignKey(Node, related_name='destinationMessages')
    
    
    
    def getActiveTrack(self):
        #El ultimo track es el activo
        #return self.tracks[0]
        return None
    
    
    
    

        