"""Feed APIs for Starling Bank transactions."""

from datetime import datetime, timedelta
import pytz
from .base_api import get


def get_transactions_for_category(access_token, account_uid, category_uid):
    """
    Get all transactions for space.

    Requires the `transaction:read` OAuth scope.

    Args:
        access_token: Starling API access token.
        account_uid: Account unique identifier.
        category_uid: Category/space unique identifier.

    Returns:
        Dictionary containing transaction feed items or None on error.
    """
    query_items = {"changesSince": three_months_ago()}
    endpoint = f"/api/v2/feed/account/{account_uid}/category/{category_uid}"
    response = get(access_token, endpoint, query_items)
    return response


def three_months_ago():
    """
    Get the datetime three months ago in ISO 8601 format.

    Returns:
        ISO 8601 formatted datetime string with timezone offset.
    """
    now = datetime.now(pytz.timezone("Europe/London"))
    offset = timedelta(weeks=13)
    result_datetime = now - offset
    iso8601_with_offset = result_datetime.isoformat()
    return iso8601_with_offset
