#!/usr/bin/env python3
"""script for testing connection to database"""
import pyodbc
import sys
import os

driver = os.environ.get('CONTACT_SQL_DRIVER')
server = os.environ.get('CONTACT_SQL_SERVER')
database = os.environ.get('CONTACT_SQL_DB')
username = os.environ.get('CONTACT_SQL_USER')
password = os.environ.get('CONTACT_SQL_PASS')
statement = sys.argv[1]
conn_str = 'Driver={};Server={};Database={};Uid={};Pwd={};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'.format(driver, server, database, username, password)
print(conn_str)
cnxn = pyodbc.connect(conn_str)
print("connected to database")
cursor = cnxn.cursor()
cursor.execute(statement)
row = cursor.fetchall()
for r in row:
    print(r)
