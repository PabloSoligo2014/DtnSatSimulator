'''
Created on 23 de ago. de 2016

@author: pabli
'''

from django.db import models
from DtnSatSimulator.models.Message import Message

class Track(models.Model):
    created = models.DateField(auto_now_add=True)
    message = models.ForeignKey(Message, related_name='tracks')

    
    