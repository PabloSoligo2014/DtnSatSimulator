'''
Created on 23 de ago. de 2016

@author: pabli
'''


from django.contrib import admin
from DtnSatSimulator.models.Satellite import Satellite
from DtnSatSimulator.models.Constellation import Constellation
from DtnSatSimulator.models.GroundStation import GroundStation
from DtnSatSimulator.models.Hope import Hope
from DtnSatSimulator.models.Message import Message
from DtnSatSimulator.models.Node import Node
from DtnSatSimulator.models.Orbit import Orbit
from DtnSatSimulator.models.Simulation import Simulation
from DtnSatSimulator.models.Track import Track


class ConstellationAdmin(admin.ModelAdmin):
    pass

class GroundStationAdmin(admin.ModelAdmin):
    pass

class HopeAdmin(admin.ModelAdmin):
    pass

class MessageAdmin(admin.ModelAdmin):
    pass

class NodeAdmin(admin.ModelAdmin):
    pass

class OrbitAdmin(admin.ModelAdmin):
    pass

class SimullationAdmin(admin.ModelAdmin):
    pass

class TrackAdmin(admin.ModelAdmin):
    pass


class SatelliteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Satellite, SatelliteAdmin)
admin.site.register(Constellation, ConstellationAdmin)
admin.site.register(GroundStation, GroundStationAdmin)
admin.site.register(Hope, HopeAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Node, NodeAdmin)
admin.site.register(Orbit, OrbitAdmin)
admin.site.register(Simulation, SimullationAdmin)
admin.site.register(Track, TrackAdmin)
