""" A collection of utility methods. """

import locale
import io
import datetime
import logging

def find_spending_space(name, spaces):
    """ Finds the first spending space with the given name. """
    result = next((item for item in spaces['spendingSpaces'] if item['name'] == name), None)

    if result is None:
        logging.error("No dictionary with 'name' equal to '%s' found.", name)
        return None

    return result
    
def find_saving_space(name, spaces):
    """ Finds the first saving space with a given name. """
    result = next((item for item in spaces['savingsGoals'] if item['name'] == name), None)

    if result is None:
        logging.error("No dictionary with 'name' equal to '%s' found.", name)
        return None
    
    return result
    
def find_first_account_uid(accounts_data):
    """ Returns the first account's UID. """
    if len(accounts_data["accounts"]) == 0:
        logging.error('No accounts found')
        return None

    return accounts_data["accounts"][0]["accountUid"]

def currency_string(minor_units):
    """ Converts an amount in minor units to a pretty string. """
    if is_raspberry_pi():
        locale.setlocale(locale.LC_ALL, 'en_GB.utf8')
    else:
        locale.setlocale(locale.LC_ALL, 'en_GB')
        
    return locale.currency(minor_units / 100.0, grouping=True)

def is_raspberry_pi():
    """ Returns whether the script is running on a Raspberry Pi or not. """
    try:
        with io.open('/sys/firmware/devicetree/base/model', 'r') as m:
            if 'raspberry pi' in m.read().lower(): return True
    except Exception: pass
    return False

def date_from_iso_8601_string(date_str):
    """ Converts an ISO 8601 date string into a timedate. """
    return datetime.datetime.fromisoformat(date_str)
