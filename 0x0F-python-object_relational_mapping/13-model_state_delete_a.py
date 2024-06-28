#!/usr/bin/python3
"""states"""

from model_state import Base, State
from sqlalchemy import create_engine, Session
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    username, password, db_name = sys.argv[1:]
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}')
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = SessionLocal()
    states_to_delete = session.query(
        State).filter(State.name.like('%a%')).all()
    for state in states_to_delete:
        session.delete(state)
    session.commit()
    session.close()
