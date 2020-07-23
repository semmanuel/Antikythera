import sqlite3
from database_creation import *

'''The script shall handle the variables needed for coordinates calculation'''


#Create a variable handling the celestial bodies' sizes
class Planet:
  def __init__ (self, mass,	diameter,	density,
                gravity	,escape_velocity,	rotation_period,	length_of_day,	distance_from_sun,	perihelion,	aphelion,
                orbital_period,	orbital_velocity,	orbital_inclination,	orbital_eccentricity,	obliquity_to_orbit,
                mean_temperature,	surface_pressure,	number_of_moons,	has_ring_system,	has_global_magnetic_field):
    self.mass= mass
    self.diameter= diameter
    self.density= density
    self.gravity= gravity
    self. escape_velocity = escape_velocity
    self.rotation_period=rotation_period
    self.length_of_day = length_of_day
    self.distance_from_sun=distance_from_sun
    self.perihelion=perihelion
    self.aphelion=aphelion
    self.orbital_period=orbital_period
    self.orbital_velocity=orbital_velocity
    self.orbital_inclination=orbital_inclination
    self.orbital_eccentricity=orbital_eccentricity
    self.obliquity_to_orbit=obliquity_to_orbit
    self.mean_temperature=mean_temperature
    self.surface_pressure=surface_pressure
    self.number_of_moons=number_of_moons
    self.has_ring_system=has_ring_system
    self.has_global_magnetic_field=has_global_magnetic_field



'''Create each planet'''
database = sqlite3.connect("celestial_objects.db")
cursor=database.cursor()
def querying(planet:str):
  cursor.execute("""SELECT * FROM CELESTIAL_OBJECTS 
  WHERE PLANET= ?;""",(planet,))
  query_result = cursor.fetchone()
  return Planet (query_result[2],
                query_result[3],
                query_result[4],
                query_result[5],
                query_result[6],
                query_result[7],
                query_result[8],
                query_result[9],
                query_result[10],
                query_result[11],
                query_result[12],
                query_result[13],
                query_result[14],
                query_result[15],
                query_result[16],
                query_result[17],
                query_result[18],
                query_result[19],
                query_result[20],
                query_result[21])

mercury=querying ('Mercury')
venus=querying   ('Venus')
earth=querying   ('Earth')
mars=querying    ('Mars')
jupiter=querying ('Jupiter')
saturn=querying  ('Saturn')
neptune= querying('Neptune')
uranus=querying  ('Uranus')
pluto=querying   ('Pluto')
#create the sun class


#create a distance scale

'''print(query_result[0][1])
for i in query_result:
  print(i)
'''


