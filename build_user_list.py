#!/usr/bin/env python3
"""script for testing connection to database"""
import pyodbc
import sys
import os
from models.user import User

driver = os.environ.get('CONTACT_SQL_DRIVER')
server = os.environ.get('CONTACT_SQL_SERVER')
database = os.environ.get('CONTACT_SQL_DB')
username = os.environ.get('CONTACT_SQL_USER')
password = os.environ.get('CONTACT_SQL_PASS')
try:
    statement = "SELECT * FROM {}".format(sys.argv[1])
except:
    print("please provide a table as an argument")
    print("usage: ./build_list.py user_table_name")
    exit(1)

needed = [driver, server, database, username, password, statement]
for req in needed:
    if req is None:
        print('Failed to get variable from env settings')
        exit(1)

# build the connection string after verifying attributes were provided
conn_str = 'Driver={};Server={};Database={};Uid={};Pwd={};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'.format(
            driver,
            server,
            database,
            username,
            password)
cnxn = pyodbc.connect(conn_str)
cursor = cnxn.cursor()
cursor.execute(statement)
row = cursor.fetchall()
for r in row:
    u = User(r[1], r[2], r[3], r[4])
    print(u)
