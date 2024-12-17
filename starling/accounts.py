""" Account APIs """

from .base_api import get

def get_accounts(access_token):
   """
   Gets all accounts.
   Requires `account:read` & `account-list:read` OAuth scopes.
   """
   response = get(access_token, "/api/v2/accounts")
   return response

def get_spaces(access_token, account_uid):
   """
   Get all spaces for accounts.
   Requires the `space:read` OAuth scope.
   """
   response = get(access_token, "/api/v2/account/" + account_uid + "/spaces")
   return response

def get_recurring_transfer(access_token, account_uid, space_uid):
   """
   Get the recurring transfer for a space.
   Requires the `savings-goal-transfer:read` OAuth scope.
   """
   response = get(access_token, "/api/v2/account/" + account_uid + "/savings-goals/" + space_uid + "/recurring-transfer")
   return response