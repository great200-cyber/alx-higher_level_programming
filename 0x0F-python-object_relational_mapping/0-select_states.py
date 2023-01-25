#!/usr/bin/python3
"""Script that prints all states in the database"""
import MySQLdb
import sys

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306,
                        user=sys.argv[1], passwd=sys.argv[2],
                        db=sys.argv[3], charset="utf8")
    cr = db.cursor()
    cr.execute("SELECT * FROM states ORDER BY states.id")
    res = cr.fetchall()
    for rows in res:
        print(rows)
    cr.close()
    db.close()
