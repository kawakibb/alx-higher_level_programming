#!/usr/bin/python3
"""
Defines the State class and Base object for SQLAlchemy ORM.

This module includes the State class, representing states with id and name attributes,
and the Base object, an instance of declarative_base() with custom metadata.
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

# Custom metadata instance
mymetadata = MetaData()

# Base object for declarative ORM
Base = declarative_base(metadata=mymetadata)

class State(Base):
    """
    SQLAlchemy model for the 'states' table with id and name attributes.
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
