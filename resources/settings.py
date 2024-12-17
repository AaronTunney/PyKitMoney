""" Manages PyKitMoney's read-only settings """

import json
import os

def name():
    """ Returns the child's name. """
    return settings().get('name')

def settings():
    """ Returns all settings in a dictionary. """
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../resources/settings.json')
    
    # Open and load the JSON file
    with open(path, 'r') as file:
        data = json.load(file)

    # Use the data (example: printing it)
    print(data)

    return data
