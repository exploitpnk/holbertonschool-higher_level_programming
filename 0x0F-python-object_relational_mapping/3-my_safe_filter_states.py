#!/usr/bin/python3
"""
    Prevent SQL Injection use "execute" with %s
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
    SELECT id, name FROM states WHERE
    name COLLATE latin1_general_cs LIKE
    %s ORDER BY id ASC;
    """
    cur.execute(sql, (argv[4], ))

    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
