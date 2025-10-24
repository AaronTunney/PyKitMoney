"""A collection of utility methods for PyKitMoney."""

import locale
import io
import datetime
import logging


def find_spending_space(name, spaces):
    """
    Find the first spending space with the given name.

    Args:
        name: Name of the spending space to find.
        spaces: Dictionary containing 'spendingSpaces' list.

    Returns:
        Dictionary of the spending space or None if not found.
    """
    result = next((item for item in spaces["spendingSpaces"] if item["name"] == name), None)

    if result is None:
        logging.error("No dictionary with 'name' equal to '%s' found.", name)
        return None

    return result


def find_saving_space(name, spaces):
    """
    Find the first saving space with a given name.

    Args:
        name: Name of the saving space to find.
        spaces: Dictionary containing 'savingsGoals' list.

    Returns:
        Dictionary of the saving space or None if not found.
    """
    result = next((item for item in spaces["savingsGoals"] if item["name"] == name), None)

    if result is None:
        logging.error("No dictionary with 'name' equal to '%s' found.", name)
        return None

    return result


def find_first_account_uid(accounts_data):
    """
    Return the first account's UID.

    Args:
        accounts_data: Dictionary containing 'accounts' list.

    Returns:
        String of the account UID or None if no accounts found.
    """
    if len(accounts_data["accounts"]) == 0:
        logging.error("No accounts found")
        return None

    return accounts_data["accounts"][0]["accountUid"]


def currency_string(minor_units):
    """
    Convert an amount in minor units to a pretty string.

    Args:
        minor_units: Amount in minor currency units (e.g., pence).

    Returns:
        Formatted currency string.
    """
    if is_raspberry_pi():
        locale.setlocale(locale.LC_ALL, "en_GB.utf8")
    else:
        locale.setlocale(locale.LC_ALL, "en_GB")

    return locale.currency(minor_units / 100.0, grouping=True)


def is_raspberry_pi():
    """
    Return whether the script is running on a Raspberry Pi.

    Returns:
        True if running on a Raspberry Pi, False otherwise.
    """
    try:
        with io.open("/sys/firmware/devicetree/base/model", "r", encoding="utf-8") as m:
            if "raspberry pi" in m.read().lower():
                return True
    except Exception:  # pylint: disable=broad-except
        pass
    return False


def date_from_iso_8601_string(date_str):
    """
    Convert an ISO 8601 date string into a datetime.

    Args:
        date_str: ISO 8601 formatted date string.

    Returns:
        datetime object.
    """
    return datetime.datetime.fromisoformat(date_str)
