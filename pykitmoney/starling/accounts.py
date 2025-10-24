"""Account APIs for Starling Bank."""

from .base_api import get


def get_accounts(access_token):
    """
    Get all accounts.

    Requires `account:read` & `account-list:read` OAuth scopes.

    Args:
        access_token: Starling API access token.

    Returns:
        Dictionary containing account information or None on error.
    """
    response = get(access_token, "/api/v2/accounts")
    return response


def get_spaces(access_token, account_uid):
    """
    Get all spaces for accounts.

    Requires the `space:read` OAuth scope.

    Args:
        access_token: Starling API access token.
        account_uid: Account unique identifier.

    Returns:
        Dictionary containing spaces information or None on error.
    """
    response = get(access_token, f"/api/v2/account/{account_uid}/spaces")
    return response


def get_recurring_transfer(access_token, account_uid, space_uid):
    """
    Get the recurring transfer for a space.

    Requires the `savings-goal-transfer:read` OAuth scope.

    Args:
        access_token: Starling API access token.
        account_uid: Account unique identifier.
        space_uid: Space unique identifier.

    Returns:
        Dictionary containing recurring transfer information or None on error.
    """
    endpoint = f"/api/v2/account/{account_uid}/savings-goals/{space_uid}/recurring-transfer"
    response = get(access_token, endpoint)
    return response
