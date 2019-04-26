#!/usr/bin/env python3
"""user class"""
from models.base_model import BaseModel

class User(BaseModel):
    """user class"""
    first_name = ""
    last_name = ""
    email = ""
    phone = ""

    def __str__(self):
        return "Name: {} {}\nEmail: {}\nPhone: {}\n".format(
                self.first_name,
                self.last_name,
                self.email,
                self.phone)
