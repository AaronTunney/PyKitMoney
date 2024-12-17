""" Displays a Starling Kite space's balance and transactions on a Raspbery Pi Zero and Waveshare 2.13" e-paper display. """

import os
import logging
from starling import accounts, feed
from resources import secrets, settings
import utils
import epaper_drawing

TRANSACTION_COUNT = 3
PIC_PATH = 'pic'

picdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), PIC_PATH)

def main():
    """ Entry point for script """
    logging.basicConfig()
    logging.getLogger().setLevel(logging.INFO)

    access_token = secrets.access_token()
    name = settings.name()

    print(name)

    if len(access_token) == 0:
        logging.warning('Access token length is 0.')

    # Get accounts data for the account Uid
    logging.info('Getting accounts')
    accounts_data = accounts.get_accounts(access_token)
    if accounts_data:
        account_uid = utils.find_first_account_uid(accounts_data)
        if account_uid:
            # Get all spaces
            logging.info('Getting spaces')
            all_spaces = accounts.get_spaces(access_token, account_uid)
            space = utils.find_spending_space(name, all_spaces)

            # Assuming GBP
            balance = utils.currency_string(space['balance']['minorUnits'])

            space_uid = space['spaceUid']

            # Get transactions for space
            logging.info('Getting transactions')
            transactions = feed.get_transactions_for_category(access_token, account_uid, space_uid)

            latest_transactions = []
            for transaction in transactions['feedItems'][:TRANSACTION_COUNT]:
                date = utils.date_from_iso_8601_string(transaction['updatedAt'])
                date_str = date.strftime("%d %b")
                sign = '-'
                if transaction['direction'] == 'IN':
                    sign = '+'
                amount_str = sign + utils.currency_string(transaction['amount']['minorUnits'])
                transaction_str = date_str + ' ' + amount_str
                latest_transactions.append(transaction_str)

            # Get next transfer
            logging.info('Getting recurring transfer')
            recurring_transfer = accounts.get_recurring_transfer(access_token, account_uid, space_uid)

            transfer_amount = utils.currency_string(recurring_transfer['currencyAndAmount']['minorUnits'])
            next_transfer = 'Next: ' + transfer_amount

            draw_to_display(name, balance, latest_transactions, next_transfer)

def draw_to_display(name, balance, transactions, next_transfer):
    """ Draws the data to the 250x122 e-paper display."""
    logging.info('Drawing %s %s %s %s', name, balance, transactions, next_transfer)

    if utils.is_raspberry_pi() is False:
        return

    epaper_drawing.draw_to_epaper_display(name, balance, transactions, next_transfer)
        
if __name__ == "__main__":
    main()
