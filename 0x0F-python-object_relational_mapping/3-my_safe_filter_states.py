#!/usr/bin/python3
"""
doc
"""
from sys import argv
from MySQLdb import connect

if __name__ == '__main__':
    init = connect(user=argv[1], passwd=argv[2],
                   db=argv[3], host="localhost", port=3306)
    query = init.cursor()
    state = argv[4]
    search = "SELECT * FROM states WHERE name LIKE %s ORDER BY states.id ASC"
    query.execute(search, [state])

    results = query.fetchall()

    for row in results:
        print(row)

    query.close()
    init.close()
