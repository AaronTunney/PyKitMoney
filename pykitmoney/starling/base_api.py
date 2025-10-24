"""Basic HTTP requests for Starling Bank API."""

import requests
import logging

BASE_URL = "https://api.starlingbank.com"


def get(access_token, endpoint, query_items=None):
    """
    Perform HTTP GET request to Starling API.

    Args:
        access_token: Starling API access token.
        endpoint: API endpoint path.
        query_items: Optional dictionary of query parameters.

    Returns:
        JSON response data or None on error.
    """
    # Define the API endpoint URL
    url = BASE_URL + endpoint

    # Set up the headers with your access token
    headers = {"Authorization": f"Bearer {access_token}"}

    try:
        # Send a GET request to the API endpoint
        response = requests.get(url=url, params=query_items, headers=headers, timeout=30)

        # Check if the request was successful (status code 200)
        if response.status_code != 200:
            logging.error("Request failed with status code %d", response.status_code)
            return None

        # Parse the JSON response
        data = response.json()
        return data

    except requests.exceptions.RequestException as e:
        logging.error("Request error: %s", e)
        return None
