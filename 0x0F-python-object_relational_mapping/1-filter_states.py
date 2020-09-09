#!/usr/bin/python3
"""
    lists all states with a name starting with N
    (upper N) from the database hbtn_0e_0_usa
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
    cur.execute("""SELECT id, name FROM states WHERE
         name COLLATE latin1_general_cs LIKE
         'N%' ORDER BY id ASC;""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
