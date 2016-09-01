'''
Created on 21 de ago. de 2016

@author: pabli
'''

import math
import DtnSatSimulator.Utils.Constants

#G = 6.67300e-11 # m3 kg-1 s-2
    
    
#cgs centrimetros, gramos, segundos
#Pyorbital puede funcionar tambien    
    
def PeriodToSemiaxis(Period):
    GM = DtnSatSimulator.Utils.Constants.G*DtnSatSimulator.Utils.Constants.Me
    a = (Period**2*(GM)/4*math.pi**2)**(1/3.0)
    return a

def AttitudeToPeriod(Semiaxis):
    #Calculate the orbital period and the speed of a satellite in oribt around
    #a massive object of mass M at a distance r from the centre of mass M.
    #pi
    #gravitational constant in mks units
    #get r
    
    #Si semiaxis esta en kilometros lo tengo que pasar a centrimetros
    Semiaxis = Semiaxis * 1000 * 100
    
    GM = DtnSatSimulator.Utils.Constants.G*DtnSatSimulator.Utils.Constants.Me
    T= math.sqrt( ((4*math.pi**2)*Semiaxis**3/(GM) ) )/60.0 #[minutos]
    
    #The period in years is T divided by the number of seconds in a year.
    TF = (24*60)/T
    #The speed for a circular orbit of radius r
    
    return TF
    
    