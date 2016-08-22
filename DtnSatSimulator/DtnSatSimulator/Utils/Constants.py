#Copyright 2008 Erik Tollerud
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

"""

=============================================================
constants -- physical constants and cosmological calculations
=============================================================

The :mod:`constants` module contains attributes storing physical constants and
conversion factors. Most of these are at the package level and should be
imported as::

    from astropysics.constants import c,G,ergperev

The following constants are included (all in cgs units):

* `G`: Newton's gravitational constant
* `mp`: proton mass
* `me`: electron mass
* `e`: electron charge
* `Ms`: solar mass
* `Mj`: jupiter mass
* `Me`: earth mass
* `Rs`: solar radius
* `Rj`: jupiter radius
* `Re`: mean earth radius
* `Rea`: equatorial earth radius (as defined by WGS84)
* `Reb`: polar earth radius (as defined by WGS84)
* `Lsun`: solar luminosity
* `kb`: boltzmann's constant
* `Rb`: gas constant
* `c`: speed of light - exact
* `h`: planck's constant
* `hbar`: reduced planck's constant
* `g0`: mean earth gravitational acceleration at sea level

The following unit conversion factors are also provided:

* `ergperev`
* `secperday`
* `secperyr`
* `secpergyr`
* `cmperpc`
* `pcpercm`
* `lyperpc`
* `pcperly`
* `cmperau`
* `aupercm`
* `asecperrad`
* `auperpc` (same as `asecperrad`)

Additional, convinience or derived values include:

* `GMskm`: Standard gravitational parameter for the sun in km^3 s^-2
* `GMsau`: Standard gravitational parameter for the sun in AU km^2 s^-2
* `GMspc`: Standard gravitational parameter for the sun in pc km^2 s^-2

The package also includes classes representing various cosmologies that are used
to derive relevant cosmological parameters. The current default is the
:class:`WMAP7Cosmology`, based on the LCDM cosmology with parameters favored by
`WMAP7 <http://lambda.gsfc.nasa.gov/product/map/dr4/parameters.cfm>`_ . 

The cosmological parameters for the builtin cosmologies are: 

* `H0`: Hubble's constant (all cosmologies)
* `h`: H0/100 (all cosmologies)
* `h7`: H0/70 (all cosmologies)
* `omega`: Total energy density as a fraction of the critical density (any FRW)
* `omegaR`: radiataion desnity (any FRW)
* `omegaM`: total matter density (any FRW)
* `omegaL`: dark energy/cosmological constant density (any FRW)
* `omegaK`: curvature density (any FRW)
* `sigma8`: rmc density fluctuation amplitude at 8 Mpc/h (WMAP)
* `omegaB`: Baryon density (WMAP)
* `omegaC`: dark/non-baryonic matter density (WMAP)
* `ns`: primordial power spectrum index (WMAP)
* `t0`: Age of universe in Gyr (WMAP)

The currently active cosmology will export it's parameters so they should be
used in other modules as::

    from astropysics.constants import H0,omega

.. todo:: examples for cosmologies, particularly :func:`rhoC`


Classes and Inheritance Structure
---------------------------------

.. inheritance-diagram:: astropysics.constants
   :parts: 1

Module API
----------

"""

from __future__ import division,with_statement
from math import pi
import numpy as np

#<--------------------------------Constants------------------------------------>
#all in cgs including gaussian esu for charge
unit_system='cgs'

G = 6.673e-8 #Netwon's gravitational constant
mp = 1.67262171e-24 #proton mass
me = 9.1093897e-28 #electron mass
e = 4.8032068e-10 #electron charge
Ms = 1.9891e33 #solar mass
Mj = 1.8986e30 #jupiter mass
Me = 5.9742e27 #earth mass
Rs = 6.96e10 #solar radius
Rj = 7.1492e9 #jupiter radius
Re = 6.371e8 #mean earth radius
Rea = 6.378137e8 #equatorial earth radius (as defined by WGS84)
Reb = Rea*(1-1/298.257223563) #polar earth radius (as defined by WGS84)
Lsun = 3.839e33 #solar luminosity
kb = 1.3807e-16 #boltzmann's constant
Rb = 8.314472e7 #gas constant
c = 2.99792458e10 #speed of light - exact
h = 6.626068E-27 #planck's constant
hbar = h/2/pi #reduced planck's constant
g0 = 980.665 #mean earth gravitational acceleration at sea level

#<-------------------------------Conversions----------------------------------->
ergperev = 1.60217646e-12
secperday = 86400 #IAU standard
secperyr = 365.25*secperday#3.15576926e7
secpergyr = secperyr*1e9
cmperpc = 3.08568025e18
pcpercm = 1.0/cmperpc
lyperpc = 3.26
pcperly = 1.0/lyperpc
cmperau = 1.49597887e13
aupercm = 1.0/cmperau
asecperrad = 206264.8062470963551564734
auperpc = asecperrad #definitionally true

#<----------------------Derived/Convinience------------------------------------>
GMskm = 1.3271244002e11 #km^3 s^-2 - from http://ssd.jpl.nasa.gov/?constants
GMsau = GMskm * aupercm * 1e5 #AU km^2 s^-2
GMspc = GMskm * pcpercm * 1e5 #pc km^2 s^-2
