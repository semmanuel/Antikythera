#r1 is the distance of the origin planet from the sun
#r2 is the distance of the destination planet from the sun
#p1 and p2 are the orbital periods of the planets

import math

def transferwindow(r1,r2,p1,p2):

    GM = 1.327E+11 #GM is the gravitational constant times the mass  of the sun

    #Converting orbital periods into seconds
    p1 = p1 * 86400
    p2 = p2 * 86400

    #Calculate the semi major axis of transfer orbit
    a = (r1 + r2) / 2

    #Calculate period of transfer orbit

    P = math.sqrt((4*(3.14 ** 2)* (a ** 3))/GM)

    #Calculate the velocity of orbit of origin planet

    v1 = (2*3.14*r1)/p1

    #Calculate the velocity of orbit of destination planet

    v2 = (2*3.14*r2)/p2

    #Calculate the velocity of transfer orbit at perihilion

    vp = ((2*3.14*a)/P) * math.sqrt(((2*a)/r1)-1)

    #Calculate the change in velocity need to go from orbit of origin planet to transfer orbit

    deltav1 = vp - v1

    # Calculate the velocity of transfer orbit at aphelion

    va = ((2*3.14*a)/P) * math.sqrt(((2*a)/r2)-1)

    #Calculate the change in velocity needed to go from transfer orbit to orbit of destination planet

    deltav2 = v2 - va

    #Calculate Time of Flight

    TOF = 0.5 * P
    TOF = TOF/86400
    TOF_months = TOF/30
    TOF_years = TOF_months/12

    print('TOF in days: ', TOF , '\nTOF in months: ', TOF_months, '\nTOF in years: ', TOF_years)



transferwindow(149600000, 57910000, 365.25636, 87.66144)