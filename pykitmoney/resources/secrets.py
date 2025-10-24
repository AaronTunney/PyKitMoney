"""Manages PyKitMoney's secrets."""

import os


def access_token():
    """
    Return the user's access token.

    Reads from ../resources/accesstoken.txt file.

    Returns:
        String containing the access token, stripped of whitespace.
    """
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../resources/accesstoken.txt")
    with open(path, "r", encoding="utf-8") as file:
        return file.read().strip(" \t\n\r")
