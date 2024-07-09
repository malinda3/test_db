from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, Session
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "postgresql://admin:password@db/dating_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

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

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
