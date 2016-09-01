'''
Created on Aug 24, 2016

@author: ubuntumate
'''

from django.db import models
from DtnSatSimulator.models.Satellite import Satellite

space = " "
newline = "\n"

class Tle(models.Model):
    tleDateTime = models.DateTimeField(auto_now_add=True)
    downloaded = models.DateTimeField(auto_now_add=True)
    
    lines = models.TextField(max_length=124, )
    


    satellite = models.ForeignKey(Satellite, related_name='tles')
    
    """
    
    def setTle(self, eccentricity, semimajorAxis, inclination, longitudeAscendingNode, argumentOfPeriapsis, meanAnomaly):
        #line1 = "1"+space+str(self.satellite.noradId)
        
        line1 = '{:1s} {:1s} {:5s}'.format('1', 'U', str(self.satellite.noradId))
        line2 = ""
        
        self.lines = line1+newline+line2
        print(self.lines)
        
    
    """
    class Meta:
        get_latest_by = "tleDateTime"  #latest() method
    
    
    """
    created     = models.DateTimeField(editable=False)
    modified    = models.DateTimeField()

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(User, self).save(*args, **kwargs)
    """
    