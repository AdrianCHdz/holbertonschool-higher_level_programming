#!/usr/bin/python3
"""
docs
"""
from sys import argv
from MySQLdb import connect

if __name__ == '__main__':
    init = connect(user=argv[1], passwd=argv[2],
                   db=argv[3], host="localhost", port=3306)
    query = init.cursor()

    state = argv[4]

    search = """SELECT cities.name
                FROM cities INNER JOIN states
                ON cities.state_id = states.id
                AND states.name LIKE %s
                ORDER BY state_id"""

    query.execute(search, [state])

    results = query.fetchall()
    """
    for row in results:
        print("{}".format(row[0]), end=", ")
    """
    print(", ".join([row[0] for row in results]))
    query.close()
    init.close()
