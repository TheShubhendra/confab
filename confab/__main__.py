import os
from confab.accounts import *


username = os.environ.get("CONFAB_USERNAME")
password = os.environ.get("CONFAB_PASSWORD")
if username is None or password is None:
    print("You are not Logged in")
    choice = input(
        """PLEASE SELECT A OPTION
1. Log in 
2. Register
press any other key to exit\n"""
    )
    if choice == "1":
        login()
    elif choice == "2":
        register()
    else:
        exit()
