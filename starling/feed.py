""" Feed APIs """

from datetime import datetime, timedelta
import pytz
from .base_api import get

def get_transactions_for_category(access_token, account_uid, category_uid):
   """
   Gets all transactions for space.
   Requires the `transaction:read` OAuth scope.
   """
   query_items = { "changesSince": three_months_ago() }
   response = get(access_token, "/api/v2/feed/account/" + account_uid + "/category/" + category_uid, query_items)
   return response

def three_months_ago():
    """ Gets the timedate three months ago. """
    now = datetime.now(pytz.timezone('Europe/London'))
    offset = timedelta(weeks=13)
    result_datetime = now - offset
    iso8601_with_offset = result_datetime.isoformat()
    return iso8601_with_offset
