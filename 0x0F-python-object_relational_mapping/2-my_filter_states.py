#!/usr/bin/python3
"""Script that displays all states matching
    argument"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database_name = argv[3]
    searched_name = argv[4]

    connect_db = MySQLdb.connect(host="localhost",
                                 port=3306,
                                 user=username,
                                 passwd=password,
                                 db=database_name)

    cursor = connect_db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id"
                .format(searched_name))
    return_list = cursor.fetchall()
    for row in return_list:
        print(row)
    cursor.close()
    connect_db.close()
