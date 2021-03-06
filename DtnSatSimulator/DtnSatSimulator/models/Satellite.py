'''
Created on 19 de ago. de 2016

@author: pabli
'''


from datetime import *
from requests import *
import ephem

from DtnSatSimulator.models.Node import Node
from DtnSatSimulator.models.Orbit import Orbit
from DtnSatSimulator.models.Parameter import Parameter
from django.utils.timezone import datetime, now, timedelta, utc
from sgp4.io import twoline2rv
from sgp4.earth_gravity import wgs72
from django.db import models

class Satellite(Node):

    #code           = models.CharField('Codigo del satelite', max_length=24, help_text='Codigo del satelite, ejemplo FS2017', unique=True)
    #description    = models.CharField('Decripcion del satelite', max_length=100, help_text='Decripcion del satelite', unique=True)
    noradId        = models.IntegerField('Codigo norad del satelite', help_text='Codigo norad del satelite', unique=True)
    active         = models.BooleanField('Activacion/desactivacion del satelite', default=True)
    notes          = models.TextField('Observaciones sobre el satelite', max_length=512, null=True) 
    #dtLaunch       = models.IntegerField("Ano de lanzamiento, dos ultimos digitos, necesarios para crear TLE", default=17)
    dtLaunch       = models.DateTimeField(auto_now_add=True)
    
    @classmethod
    def new(cls, code, description, noradId):
        result = cls()
        result.code        = code
        result.description = description
        result.noradId     = noradId
        return result
    
    def getCode(self):
        return self.code
    
    
    """
    Metodo privado doble __
    """
    def __downloadLastTle(self):
        #Solo me traigo el tle si hace un dia que no me lo traigo
        from DtnSatSimulator.models.Tle import Tle
        try:
            loginURL = Parameter.objects.get(key="NoradLoginURL")
        except Parameter.DoesNotExist:
            loginURL = None
            
        if loginURL==None:
            loginURL = Parameter()
            loginURL.key = "NoradLoginURL"
            loginURL.value = "https://www.space-track.org/ajaxauth/login"
            loginURL.module = "Temporal"
            loginURL.save()
            
        try:
            username = Parameter.objects.get(key="NoradUserName")
        except Parameter.DoesNotExist:
            username = None
            
        if username==None:
            username = Parameter()
            username.key = "NoradUserName"
            username.value = "macecilia"
            username.module = "Temporal"
            username.save()
        
        try:
            password = Parameter.objects.get(key="NoradPassword")
        except Parameter.DoesNotExist:
            password = None
            
        if password==None:
            password = Parameter()
            password.key = "NoradPassword"
            password.value = "MaCeciliaSpace17"
            password.module = "Temporal"
            password.save()
        
            
        #u: macecilia
        #p: MaCeciliaSpace17
    
            
        
            
        data = {'identity': username.value , 'password': password.value}
            
            
        s = session()
        rp = s.post(loginURL.value, data)
        #self.noradId noradid hardcodeado
        fquery = "https://www.space-track.org/basicspacedata/query/class/tle_latest/ORDINAL/1/NORAD_CAT_ID/" + str(self.noradId) + "/orderby/TLE_LINE1 ASC/format/tle"
        # print(s.cookies)
        rg = s.get(fquery)
            
            
        TLE = rg.text.split("\n")
        sgp4sat = twoline2rv(TLE[0], TLE[1], wgs72)  # es un objeto de clase (satelite)
            
            
        tle             = Tle()
        tle.satellite   = self
        tle.tleDateTime = sgp4sat.epoch
        tle.downloaded  = datetime.now(utc)
        tle.lines       = rg.text
        #print("Salvando TLE")
        tle.save()
        
        #param.value = (datetime.now(utc)).strftime("%B %d, %Y")
        #param.save()

    
    def getLastTLE(self):
        #Implementar que retorne el ultimo TLE, ir a buscar a los TLEs descargado
        """
        Verificar la fecha de ultima descarga del TLE, si puede existir un TLE nuevo intentar descargarlo
        """
        if (self.tles.exists()==False):
            #No hay tle debo descargar el primero
            self.__downloadLastTle()
        else:
 
            dtn = datetime.now(utc)
            delta = dtn - self.tles.last().tleDateTime
            #print("dif: ", delta.days*24*60)
            if delta.days*24*60>12:
                print("Tle no actualizado, descargar nuevo tle")
                self.__downloadLastTle()
            else:
                pass
                #TLE actualizado no hago nada! 
                #self.__downloadLastTle()   
                #print("Tle actualizado")
            
            
        return self.tles.last()

            
         

    def getCelestialPosition(self, dtm=datetime.now(utc)):
        #Implementar el metodo para que retorne la posicion instantane del satelite    
        from DtnSatSimulator.models.Propagation import Propagation
        from DtnSatSimulator.models.PropagationDetail import PropagationDetail
        
        #if PropagationDetail.objects.all().count()>0:
        #    print(PropagationDetail.objects.last().dt)
        
        min_dt = dtm - timedelta(seconds=1)
        max_dt = dtm + timedelta(seconds=1)
        #Si ya esta propagado no vuelvo a propagar
        #Asqueroso como se filtra por fecha, no hay forma mejor?? YourModel.objects.filter(datetime_published=datetime(2008, 03, 27))
        prps = PropagationDetail.objects.filter(dt__range=(min_dt, max_dt)).filter(propagation__satellite=self)
        #.filter(propagation__satellite__code=self.code) 
        #print(prps)
        #Me aseguro de tener TLE
        
        
        if prps.count()==0:        
        
            #self.__downloadLastTle()
            tle = self.getLastTLE()
        
            ls = tle.lines.split("\n") 
                
            #print("TLE0:", ls[0])
            #print("TLE1:", ls[1])
            sgp4sat = twoline2rv(ls[0], ls[1], wgs72)
        
        

            position, velocity = sgp4sat.propagate(dtm.year, dtm.month, dtm.day, dtm.hour , dtm.minute, dtm.second) #(2000, 6, 29, 12, 50, 19)
            
            propagation = Propagation()
            propagation.tle = tle
            propagation.satellite = self
            propagation.final = False
            
            
            propagationDetail = PropagationDetail()
            propagation.save()
            propagationDetail.propagation = propagation
            
            propagationDetail.positionX = position[0]
            propagationDetail.positionY = position[1]
            propagationDetail.positionZ = position[2]
            
            propagationDetail.velocityX = velocity[0]
            propagationDetail.velocityY = velocity[1]
            propagationDetail.velocityZ = velocity[2]
            propagationDetail.dt = dtm
            
            propagation.save()
            propagationDetail.save()
            
            #Primero reviso que la propagacion ya no este realizada
            return position, velocity
        else:
            
            return prps[0].positionX, prps[0].positionY, prps[0].positionZ
    
    def __str__(self):
        return self.code