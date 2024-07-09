from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    gender_id = Column(Integer, ForeignKey("genders.gender_id"))
    city_id = Column(Integer, ForeignKey("cities.city_id"))
    preference_id = Column(Integer, ForeignKey("preferences.preference_id"))
    goal_id = Column(Integer, ForeignKey("goals.goal_id"))
    description = Column(String, index=True)

class Gender(Base):
    __tablename__ = "genders"
    gender_id = Column(Integer, primary_key=True, index=True)
    gender = Column(String, unique=True)

class City(Base):
    __tablename__ = "cities"
    city_id = Column(Integer, primary_key=True, index=True)
    city = Column(String, unique=True)

class Preference(Base):
    __tablename__ = "preferences"
    preference_id = Column(Integer, primary_key=True, index=True)
    preference = Column(String, unique=True)

class Goal(Base):
    __tablename__ = "goals"
    goal_id = Column(Integer, primary_key=True, index=True)
    goal = Column(String, unique=True)
