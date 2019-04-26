#!/usr/bin/env python3
"""script for testing connection to database"""
from models.user import User
import models

users = models.storage.all()
for user in users.values():
    print(user)
print('Users count: {}'.format(len(users)))
