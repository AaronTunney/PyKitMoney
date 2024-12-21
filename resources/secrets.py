""" Manages the module's secrets. """

import os

def access_token():
    """ Returns the user's access token. """
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../resources/accesstoken.txt')
    with open(path, 'r',  encoding="utf-8") as file:
        # Read the entire file contents into a string
        return file.read().strip(' \t\n\r')
