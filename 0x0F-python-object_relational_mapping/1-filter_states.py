#!/usr/bin/python3
"""
doc
"""
from sys import argv
from MySQLdb import connect

if __name__ == '__main__':
    """
    doc
    """
    init = connect(user=argv[1], passwd=argv[2],
                   db=argv[3], host="localhost", port=3306)
    query = init.cursor()
    query.execute("""SELECT * FROM states WHERE name LIKE 'N%' ORDER BY
    states.id""")
    results = query.fetchall()
    for row in results:
        print(row)
    query.close()
    init.close()
