#!/usr/bin/python3
"""Lists states from the database hbtn_0e_0_usa that match a provided name"""

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
    
    # Get the search term from the command-line argument
    match = sys.argv[4]
    
    # Execute an SQL query to select rows from the 'states' table where the name matches the provided argument
    # The '%' symbol is a placeholder for the parameter to prevent SQL injection
    cur.execute("SELECT * FROM states WHERE name LIKE %s", (match, ))
    
    # Fetch all the rows returned by the query
    rows = cur.fetchall()
    
    # Iterate through the rows and print each row
    for row in rows:
        print(row)
    
    # Close the cursor and the database connection to release resources
    cur.close()
    db.close()

