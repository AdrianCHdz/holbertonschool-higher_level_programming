#!/usr/bin/python3
"""
focs
"""
from sys import argv
from MySQLdb import connect


if __name__ == '__main__':
    init = connect(user=argv[1], passwd=argv[2],
                   db=argv[3], host="localhost", port=3306)
    query = init.cursor()

    search = """SELECT cities.id, cities.name, states.name
                FROM cities INNER JOIN states
                ON cities.state_id = states.id
                ORDER BY state_id"""

    query.execute(search)

    results = query.fetchall()

    for row in results:
        print(row)

    query.close()
    init.close()
