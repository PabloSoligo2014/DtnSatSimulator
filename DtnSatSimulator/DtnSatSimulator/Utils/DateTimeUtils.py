'''
Created on 20 de ago. de 2016

@author: pabli
'''
from datetime import datetime
import math
from org.orekit.time import TimeScalesFactory, AbsoluteDate;

from org.hipparchus.geometry.euclidean.threed import RotationOrder;
from org.hipparchus.geometry.euclidean.threed import Vector3D;

def datetime_to_absolutedate(adatetime):
      
    utc = TimeScalesFactory.getUTC();
        
    return AbsoluteDate(adatetime.year, adatetime.month, adatetime.day, adatetime.hour,  adatetime.minute, float(adatetime.second), utc);
        
    
    
    
    

def absolutedate_to_datetime(orekit_date):

    utc = TimeScalesFactory.getUTC()
    or_comp = orekit_date.getComponents(utc)
    or_date = or_comp.getDate()
    or_time = or_comp.getTime()
    seconds = or_time.getSecond()
    return datetime(or_date.getYear(),
             or_date.getMonth(),
             or_date.getDay(),
             or_time.getHour(),
             or_time.getMinute(),
             int(math.floor(seconds)),
             int(1000.0 * (seconds - math.floor(seconds))))