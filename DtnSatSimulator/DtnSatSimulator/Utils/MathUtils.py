'''
Created on 21 de ago. de 2016

@author: pabli
'''

import math
import DtnSatSimulator.Utils.Constants

#G = 6.67300e-11 # m3 kg-1 s-2
    
    
def PeriodToSemiaxis(Period):
    a = (Period**2*(DtnSatSimulator.Utils.Constants.G*DtnSatSimulator.Utils.Constants.Me)/4*math.pi**2)**(1/3.0)
    return a

def SemiaxisToPeriod(Semiaxis):
    #Calculate the orbital period and the speed of a satellite in oribt around
    #a massive object of mass M at a distance r from the centre of mass M.
    #pi
    #gravitational constant in mks units
    #get r
    
    T= math.sqrt( ((4*math.pi**2)*Semiaxis**3/(DtnSatSimulator.Utils.Constants.G*DtnSatSimulator.Utils.Constants.Me) ) )
    
    #The period in years is T divided by the number of seconds in a year.
    T_years = T/(365.0*24.0*60.0*60.0)
    #The speed for a circular orbit of radius r
    
    return T_years
    
    