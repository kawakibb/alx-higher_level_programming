#!/usr/bin/python3
""" Lists all states from the database hbtn_0e_0_usa that start with 'N' """
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
    
    # Execute an SQL query to select rows from the 'states' table where the name starts with 'N'
    # The 'LIKE BINARY' ensures case-sensitive matching, and the results are ordered by 'id'
    cur.execute("""SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY states.id""")
    
    # Fetch all the rows returned by the query
    rows = cur.fetchall()
    
    # Iterate through the rows and print each row
    for row in rows:
        print(row)
    
    # Close the cursor and the database connection to release resources
    cur.close()
    db.close()

