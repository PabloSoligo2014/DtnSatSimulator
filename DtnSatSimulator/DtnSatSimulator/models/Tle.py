'''
Created on Aug 24, 2016

@author: ubuntumate
'''

from django.db import models
from DtnSatSimulator.models.Satellite import Satellite
from datetime import datetime

space = " "
newline = "\n"

class Tle(models.Model):
    tleDateTime = models.DateTimeField(auto_now_add=True)
    downloaded = models.DateTimeField(auto_now_add=True)
    
    lines = models.TextField(max_length=124, )
    
    satellite = models.ForeignKey(Satellite, related_name='tles')
    
   
    
    def setTle(self, eccentricity, semimajorAxis, inclination, longitudeAscendingNode, argumentOfPeriapsis, meanAnomaly):
        #line1 = "1"+space+str(self.satellite.noradId)
        
#        Example
#        ISS (ZARYA)
#        1 25544U 98067A   08264.51782528 -.00002182  00000-0 -11606-4 0  2927
#        2 25544  51.6416 247.4627 0006703 130.5360 325.0288 15.72125391563537
        
        

        year = str(datetime.now().year)[-2:]
        
        #dt = self.satellite.dtLaunch
        
        launchDay = self.satellite.dtLaunch.timetuple().tm_yday
        launchYear = str(self.satellite.dtLaunch.year)[-2:]
        
        todayDay = datetime.now().timetuple().tm_yday
        fractionDay = datetime.now().
        todayDayPart = str(todayDay)[-2:]+"."
        #         n     noradId c  year day
        line1 = '{:1s} {:5s}{:1s} {:2s}{:0>3s}{: <3s} {:2s}'.format('1', str(self.satellite.noradId), 'U', str(launchYear), str(launchDay), "A", str(todayDayPart),  )
        line2 = "" 
        
        self.lines = line1+newline+line2
        print(self.lines)
        
    
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
    