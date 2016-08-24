'''
Created on 22 de ago. de 2016

@author: pabli
'''
from django.db import models
from DtnSatSimulator.Model import Track

class Hope(models.Model):
    track = models.ForeignKey(Track)