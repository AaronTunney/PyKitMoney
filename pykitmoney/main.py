"""
Displays a Starling Kite space's balance and transactions on a Raspberry Pi Zero
and Waveshare 2.13" e-paper display.
"""

import logging
from pykitmoney.starling import accounts, feed
from pykitmoney.resources import secrets, settings
from pykitmoney import utils, epaper_drawing

TRANSACTION_COUNT = 3


def main():
    """Entry point for script."""
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    access_token = secrets.access_token()
    name = settings.name()

    print(name)

    if len(access_token) == 0:
        logging.warning("Access token length is 0.")

    # Get accounts data for the account Uid
    logging.info("Getting accounts")
    accounts_data = accounts.get_accounts(access_token)
    if accounts_data:
        account_uid = utils.find_first_account_uid(accounts_data)
        if account_uid:
            # Get all spaces
            logging.info("Getting spaces")
            all_spaces = accounts.get_spaces(access_token, account_uid)
            space = utils.find_spending_space(name, all_spaces)

            # Assuming GBP
            balance = utils.currency_string(space["balance"]["minorUnits"])

            space_uid = space["spaceUid"]

            # Get transactions for space
            logging.info("Getting transactions")
            transactions = feed.get_transactions_for_category(access_token, account_uid, space_uid)

            latest_transactions = []
            for transaction in transactions["feedItems"][:TRANSACTION_COUNT]:
                date = utils.date_from_iso_8601_string(transaction["updatedAt"])
                date_str = date.strftime("%d %b")
                sign = "-"
                if transaction["direction"] == "IN":
                    sign = "+"
                amount_str = sign + utils.currency_string(transaction["amount"]["minorUnits"])
                transaction_str = date_str + " " + amount_str
                latest_transactions.append(transaction_str)

            # Get next transfer
            logging.info("Getting recurring transfer")
            recurring_transfer = accounts.get_recurring_transfer(
                access_token, account_uid, space_uid
            )

            transfer_amount = utils.currency_string(
                recurring_transfer["currencyAndAmount"]["minorUnits"]
            )
            next_transfer = "Next: " + transfer_amount

            draw_to_display(name, balance, latest_transactions, next_transfer)


def draw_to_display(name, balance, transactions, next_transfer):
    """
    Draw the data to the 250x122 e-paper display.

    Args:
        name: The name of the space.
        balance: The balance of the space.
        transactions: A list of transaction strings.
        next_transfer: The next transfer information.
    """
    logging.info("Drawing %s %s %s %s", name, balance, transactions, next_transfer)

    if not utils.is_raspberry_pi():
        logging.info("Not running on Raspberry Pi, skipping display output")
        return

    epaper_drawing.draw_to_epaper_display(name, balance, transactions, next_transfer)


if __name__ == "__main__":
    main()
