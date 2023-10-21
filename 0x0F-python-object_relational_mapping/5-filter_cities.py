#!/usr/bin/python3
"""Lists cities in a specified state from the database hbtn_0e_0_usa"""

# Import necessary modules
import MySQLdb
import sys

# Check if the script is being run as the main program
if __name__ == "__main__":
    # Establish a connection to the MySQL database using command-line arguments
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    
    # Create a cursor for executing SQL queries
    cur = db.cursor()
    
    # Execute an SQL query to select city names by joining the 'cities' and 'states' tables
    # and filtering by the specified state name
    cur.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))
    
    # Fetch all the rows returned by the query
    rows = cur.fetchall()
    
    # Extract city names from the rows and store them in a list
    tmp = list(row[0] for row in rows)
    
    # Print the city names separated by a comma and a space
    print(*tmp, sep=", ")
    
    # Close the cursor and the database connection to release resources
    cur.close()
    db.close()
