#!/usr/bin/python3
"""
Start link class to table in the database.
"""
# Import necessary modules
import sys
from model_state import Base, State
from sqlalchemy import create_engine

# Check if the script is being run as the main program
if __name__ == "__main__":
    # Create a connection to the MySQL database using the provided arguments
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    
    # Create the database tables based on the SQLAlchemy models (if they don't already exist)
    Base.metadata.create_all(engine)
