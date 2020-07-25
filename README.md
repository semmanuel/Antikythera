# Antikythera

Physics-based, simulation of the solar system.

## Program Structure
- ``Project Process Models/`` - Design models.
- ``database_creation/`` - Files necessary for building and storing databases.
- ``practice/`` - Test builds for various components.
- ``Body.py`` - Class definition of celestial bodies and physical simulations.
- ``GUI.py`` - Class definition for User Interface, built with Pygame.
- ``main.py`` - Main program to run. Activates GUI and creates all Bodies solar system.
- ``Transferwindow.py`` - Mathematical calculation for finding transfer window period between to planets.

## Requirements
- PyCharm(Preferred IDE)
- Python3
###### Modules
- Pygame
- Numpy
- Sqlite3
- Pandas
- SQLAlchemy
- Skyfield

## Installation Set Up
*PyCharm allows you to easily install modules through File > Settings > Project: Antikythera > Project Interpreter >* ``+``.

You can also use the package manager [pip](https://pip.pypa.io/en/stable/) from command line to install all modules.
```bash
pip install pygame
pip install numpy
pip install sqlite3
pip install sqlalchemy
pip install pandas
pip install skyfield
```

Clone project, setup databases, and run main program.
```
git clone https://github.com/semmanuel/Antikythera
cd Antikythera
python3 database_creation/create_db.py  
python3 main.py
```

## Features
- Graphical simulation of the Solar System
- Search Celestial Objects (e.g Planets)
- Search Celestial Events (e.g Lunar Eclipse)
- Slow down, speed up, and pause time
- Activate orbit tracking trails
- Hover over planets for information.

## Authors
* [**Brandon Merluzzo**](https://github.com/mishakh) - merluzzob@wit.edu

* [**Carter Trafton**](https://github.com/cartertrafton) - cartertrafton@gmail.com

* [**Michael J. Leblanc**](https://github.com/mleblanc98) - leblancm4@wit.edu

* [**Rafael Da Luz Barbosa**](https://github.com/itsraf) - daluzbarbosar@wit.edu

* [**Stanley Emmanuel**](https://github.com/semmanuel) - emmanuels@wit.edu

* [**Thurein Myint**](https://github.com/trmyint97) - myintt@wit.edu


## Acknowledgments

- D. Shiffman, The Nature of the Code. [S.l.]: D. Shiffman, 2012.
