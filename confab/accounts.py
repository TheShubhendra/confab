"""Module to handle Login and Register requests"""
import os
from .helper import username_exists


def register():
    username = input("Please create your username: ")
    while username_exists(username):
        username = input("This username is not available,try again: ")
    os.environ.set("CONFAB_USERNAME")
