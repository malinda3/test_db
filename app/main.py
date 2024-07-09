from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .db import SessionLocal, Base, get_db, User

app = FastAPI()

Base.metadata.create_all(bind=SessionLocal().get_bind())

@app.get("/users/")
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = db.query(User).offset(skip).limit(limit).all()
    return users
