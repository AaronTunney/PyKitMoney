""" Basic HTTP requests """

import requests
import logging

BASE_URL = "https://api.starlingbank.com"

def get(access_token, endpoint, query_items = None):
    """ HTTP GET method. """

    # Define the API endpoint URL
    url = BASE_URL + endpoint

    # Set up the headers with your access token
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    try:
        # Send a GET request to the API endpoint
        response = requests.get(url=url, params=query_items, headers=headers, timeout=30)

        # Check if the request was successful (status code 200)
        if response.status_code != 200:
            logging.error('Request failed with status code %d', response.status_code)
            return None
        
        # Parse the JSON response
        data = response.json()
        return data
    
    except requests.exceptions.RequestException as e:
        logging.error('Request error: %e', e)
        return None
