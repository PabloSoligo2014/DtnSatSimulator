'''
Created on Aug 24, 2016

@author: ubuntumate
'''

from django.db import models
from GroundSegment.models.Satellite import Satellite


class Tle(models.Model):
    tleDateTime = models.DateTimeField(auto_now_add=True)
    downloaded = models.DateTimeField(auto_now_add=True)
    lines = models.TextField(max_length=124, )

    satellite = models.ForeignKey(Satellite, related_name='tles')
    
    
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
    