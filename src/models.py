import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    login_stattus = Column(String(250), nullable=False)
    register_date = Column(String(250), nullable=False)
    favorites= relationship("favorites", back_populates="favorites")


class Favorites(Base):
    __tablename__ = 'Favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.id'))
    plantets_id= Column(String(250))
    Movies= Column(String(250))
    Starships= Column(String(250))
    Characters= Column(String(250))
    user = relationship(User, back_populates="user")

class Planets(Base):
    __tablename__ = 'Planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    planet_id = Column(Integer, primary_key=True)
    planet_name = Column(String(250))
    planet_url = Column(String(250))
    person = relationship(Favorites)
    user_id = Column(Integer, ForeignKey('Favorites.id'))


    
class Starships(Base):
    __tablename__ = 'Starships'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    starships_id= Column(Integer, primary_key=True)
    starships_name= Column(String(250))
    starhips_url = Column(String(250))
    person = relationship(Favorites)
    user_id = Column(Integer, ForeignKey('Favorites.id'))


class Characters(Base):
    __tablename__ = 'Characters'
    characters_id = Column(Integer, primary_key=True)
    characters_name = Column(String(250))
    characters_url = Column(String(250))
    person = relationship(Favorites)
    user_id = Column(Integer, ForeignKey('Favorites.id'))


class Movies(Base):
    __tablename__ = 'Movies'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    movies_url = Column(String(250))
    person = relationship(Favorites)
    user_id = Column(Integer, ForeignKey('Favorites.id'))




    
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
