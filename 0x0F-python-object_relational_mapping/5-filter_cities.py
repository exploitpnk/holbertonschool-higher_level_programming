#!/usr/bin/python3
"""
    Lists all cities of that state, using the database hbtn_0e_4_usa
"""


import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306, user=argv[1],
        passwd=argv[2],
        db=argv[3])
    cur = db.cursor()

    sql = """
    SELECT cities.name FROM cities JOIN states ON
    cities.state_id = states.id WHERE states.name = %s
    ORDER BY cities.id ASC;
    """

    cur.execute(sql, (argv[4],))

    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
