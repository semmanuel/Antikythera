from pandas import read_csv
from sqlalchemy import create_engine
#this will convert csv files into a dataframe which it will be added to sqlalchemy and that will add a sqlite db

'''comets= read_csv("near-earth-comets_1.csv", encoding="ISO-8859-1")

engine = create_engine('sqlite:///comets.db', echo=True)
sqlite_connection = engine.connect()
sqlite_table = "COMETS"
comets.to_sql(sqlite_table, sqlite_connection, if_exists='fail')


sqlite_connection.close()
'''
#Meteor Table
meteorites= read_csv("near-earth-comets.csv", encoding="ISO-8859-1")

engine = create_engine('sqlite:///meteorites.db', echo=True)
sqlite_connection = engine.connect()
sqlite_table = "METEORITES"
meteorites.to_sql(sqlite_table, sqlite_connection, if_exists='fail')

#Eclipses Relation
lunareclipse= read_csv("lunar.csv", encoding="ISO-8859-1")

engine = create_engine('sqlite:///eclipses.db', echo=True)
sqlite_connection = engine.connect()
sqlite_table = "Lunar Eclipse"
lunareclipse.to_sql(sqlite_table, sqlite_connection, if_exists='fail')

solareclipse= read_csv("solar.csv", encoding="ISO-8859-1")
sqlite_table = "Solar Eclipse"
solareclipse.to_sql(sqlite_table, sqlite_connection, if_exists='fail')
 #Asteroids
asteroid= read_csv("impacts.csv", encoding="ISO-8859-1")

engine = create_engine('sqlite:///Asteroid.db', echo=True)
sqlite_connection = engine.connect()
sqlite_table = "Potential Asteroid impacts"
asteroid.to_sql(sqlite_table, sqlite_connection, if_exists='fail')

asteroid= read_csv("orbits.csv", encoding="ISO-8859-1")
sqlite_table = "Asteroid Orbits"
asteroid.to_sql(sqlite_table, sqlite_connection, if_exists='fail')
sqlite_connection.close()
