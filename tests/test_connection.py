#!/usr/bin/env python3
"""script for testing connection to database"""
import pyodbc as db
import sys

server = 'tcp:cutflobackupserver.database.windows.net'
database = 'users'
username = sys.argv[1]
password = sys.argv[2]
driver= '{ODBC Driver 17 for SQL Server}'


