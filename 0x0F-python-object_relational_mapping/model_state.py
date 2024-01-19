#!/usr/bin/python3
"""This module contains the class definition of a State"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """Represents state class
    Attributes:
            __tablename__: table name of the class
            id: id of state
            name: state name.
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
