import sqlite3

#from Body import Body
from database_creation import *
from Body import *


#Create an inheritance from the body, so that we can keep the x, y, c, tr
class CelestialBody(Body):
  def __init__ (self, name, x, y, r, c,  root, tr, theta, real_mass, real_diameter, real_volume, real_density,
                real_gravity, real_escape_velocity, real_rotation_period, real_length_of_day, real_distance_from_sun, real_perihelion, real_aphelion,
                real_orbital_period, real_orbital_velocity, real_orbital_inclination, real_orbital_eccentricity, real_obliquity_to_orbit,
                real_mean_temperature, real_surface_pressure, real_number_of_moons, real_has_ring_system, real_has_global_magnetic_field):
    self.name = name #None
    self.mass = real_mass #None
    self.diameter = real_diameter #None
    self.volume = real_volume
    self.density = real_density #None
    self.gravity = real_gravity #None
    self.escape_velocity = real_escape_velocity#None
    self.rotation_period = real_rotation_period#None
    self.length_of_day = real_length_of_day#None
    self.distance_from_sun = real_distance_from_sun#None
    self.perihelion = real_perihelion #None
    self.aphelion = real_aphelion#None
    self.orbital_period = real_orbital_period#None
    self.orbital_velocity = real_orbital_velocity#None
    self.orbital_inclination = real_orbital_inclination#None
    self.orbital_eccentricity = real_orbital_eccentricity#None
    self.obliquity_to_orbit = real_obliquity_to_orbit#None
    self.mean_temperature = real_mean_temperature#None
    self.surface_pressure = real_surface_pressure#None
    self.number_of_moons = real_number_of_moons#None
    self.has_ring_system = real_has_ring_system#None
    self.has_global_magnetic_field = real_has_global_magnetic_field#None
    Body.__init__( self, x, y, r, c, root, tr, theta)

  def update(self, distance_scaling, velocity_scaling):
      # update position based on velocity and reset accel if not sun
      self.sunDistance = math.sqrt((self.position[0] - 800) ** 2 + (self.position[1] - 400) ** 2)
      self.velocity = np.add(self.velocity, self.accel)
      self.last_position = self.position
      self.position = [800 + self.distance_from_sun / distance_scaling * math.cos(self.theta), 400 + self.distance_from_sun / distance_scaling * math.sin(self.theta)]
      self.accel = 0
      self.theta += (self.orbital_velocity / velocity_scaling)

  #created a classmethod functioning as a constructor, to avoid inputting manually the
  #information of every attribute of the planet
  @classmethod
  def create_planet(cls,planet_name:str, x, y, r, c, root, tr, theta):
    database = sqlite3.connect("celestial_objects.db")
    cursor = database.cursor()
    cursor.execute("""SELECT * FROM CELESTIAL_OBJECTS WHERE PLANET= ?;""",(planet_name,))
    query_result = cursor.fetchone()
    return cls (planet_name,
                x,
                y,
                r,
                c,
                root,
                tr,
                theta,
                query_result[2],
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
                query_result[21],
                query_result[22])


class Star(Body):
  def __init__(self, name, x, y, r, c, root, tr, theta, real_mass, real_volume, real_radius, real_photos_radius, real_photos_temp, real_photos_depth,
               real_flatness, real_surface_gravity, real_solar_constant, real_sunspot_cycle, real_mean_density, real_escape_velocity,
               real_effective_temp):
    self.name = name
    self.mass = real_mass,
    self.volume = real_volume
    self.radius = real_radius
    self.photos_radius = real_photos_radius,
    self.photos_temp = real_photos_temp,
    self.photos_depth = real_photos_depth,
    self.flatness = real_flatness,
    self.surface_gravity = real_surface_gravity
    self.solar_constant = real_solar_constant,
    self.sunspot_cycle = real_sunspot_cycle,
    self.mean_density = real_mean_density
    self.escape_velocity = real_escape_velocity
    self.effective_tmp = real_effective_temp
    Body.__init__(self, x, y, r, c, root, tr, theta)


  @classmethod
  def create_star(cls, star_name, x, y, r, c, root, tr, theta):
    database = sqlite3.connect("Stars.db")
    cursor=database.cursor()
    cursor.execute("""SELECT * FROM STARS 
    WHERE STAR= ?;""",(star_name,))
    query_result = cursor.fetchone()
    return cls (star_name,
                x,
                y,
                r,
                c,
                root,
                tr,
                theta,
                query_result[2],
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
                query_result[14])





