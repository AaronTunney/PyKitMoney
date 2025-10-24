"""Manages PyKitMoney's read-only settings."""

import json
import os


def name():
    """
    Return the child's name from settings.

    Returns:
        String containing the child's name.
    """
    return settings().get("name")


def settings():
    """
    Return all settings in a dictionary.

    Reads from ../resources/settings.json file.

    Returns:
        Dictionary containing all settings.
    """
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../resources/settings.json")

    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data
