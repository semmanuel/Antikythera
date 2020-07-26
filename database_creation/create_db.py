from pandas import read_csv
from sqlalchemy import create_engine
import skyfield

#this will convert csv files into a dataframe which it will be added to sqlalchemy and that will add a sqlite db

#Events database
#Eclipses Relation
def create_db():
  lunareclipse= read_csv("lunar.csv", encoding="ISO-8859-1")
  engine = create_engine('sqlite:///celestial_events.db', echo=False)
  sqlite_connection = engine.connect()
  sqlite_table = "Lunar Eclipse"
  lunareclipse.to_sql(sqlite_table, sqlite_connection, if_exists='replace')

  solareclipse= read_csv("solar.csv", encoding="ISO-8859-1")
  engine = create_engine('sqlite:///solar_eclipse.db', echo=False)
  sqlite_connection = engine.connect()
  sqlite_table = "Solar Eclipse"
  solareclipse.to_sql(sqlite_table, sqlite_connection, if_exists='replace')
  #Asteroids
  asteroid = read_csv("impacts.csv", encoding="ISO-8859-1")
  engine = create_engine('sqlite:///Asteroid.db', echo=False)
  sqlite_connection = engine.connect()
  sqlite_table = "Potential Asteroid impacts"
  asteroid.to_sql(sqlite_table, sqlite_connection, if_exists='replace')
  #Asteroid Magnitude & Diameter are present in table
  asteroid_orbits = read_csv("orbits.csv", encoding="ISO-8859-1")
  engine = create_engine('sqlite:///Asteroid_orbit.db', echo=False)
  sqlite_connection = engine.connect()
  sqlite_table = "Asteroid Orbits"
  asteroid_orbits.to_sql(sqlite_table, sqlite_connection, if_exists='replace')

  #Celestial Objects ~ Planets
  planets= read_csv("planets.csv", encoding="ISO-8859-1")
  engine = create_engine('sqlite:///celestial_objects.db', echo=False)
  sqlite_connection = engine.connect()
  sqlite_table = "celestial_objects"
  planets.to_sql(sqlite_table, sqlite_connection, if_exists='replace')
  #Comets
  comets= read_csv("near-earth-comets.csv", encoding="ISO-8859-1")
  engine = create_engine('sqlite:///near_earth_comets.db', echo=False)
  sqlite_connection = engine.connect()
  sqlite_table = "Comets"
  comets.to_sql(sqlite_table, sqlite_connection, if_exists='replace')

  #Stars, but for now populated by the Sun only
  stars=read_csv("stars.csv",encoding="ISO-8859-1")
  engine=create_engine('sqlite:///Stars.db', echo=False)
  sqlite_connection = engine.connect()
  sqlite_table = "Stars"
  stars.to_sql(sqlite_table, sqlite_connection, if_exists='replace')
  sqlite_connection.close()

