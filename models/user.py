#!/usr/bin/env python3
"""user class"""

class User():
    """user class"""
    def __init__(self, first, last, email, phone):
        self.first_name = first
        self.last_name = last
        self.email = email
        self.phone = phone

    def __str__(self):
        return "Name: {} {}\nEmail: {}\nPhone: {}\n".format(
                self.first_name,
                self.last_name,
                self.email,
                self.phone)
