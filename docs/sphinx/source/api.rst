API Overview
============

PyKitMoney provides a clean Python API for interacting with Starling Bank
and displaying information on e-paper displays.

For detailed module documentation, see :doc:`api/modules`.

Key Components
--------------

Entry Point
~~~~~~~~~~~

.. code-block:: python

   from pykitmoney import main
   
   main.main()  # Run the application

Starling API Client
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from pykitmoney.starling import accounts, feed
   
   # Get all accounts
   accounts_data = accounts.get_accounts(access_token)
   
   # Get spaces
   spaces = accounts.get_spaces(access_token, account_uid)
   
   # Get transactions
   transactions = feed.get_transactions_for_category(
       access_token, account_uid, category_uid
   )

Utility Functions
~~~~~~~~~~~~~~~~~

.. code-block:: python

   from pykitmoney import utils
   
   # Find a space by name
   space = utils.find_spending_space('Kate', spaces)
   
   # Format currency
   formatted = utils.currency_string(1234)  # "£12.34"
   
   # Parse dates
   date = utils.date_from_iso_8601_string("2024-01-15T10:30:00Z")
   
   # Check platform
   is_pi = utils.is_raspberry_pi()

Drawing Utilities
~~~~~~~~~~~~~~~~~

.. code-block:: python

   from pykitmoney import draw_utils
   
   # Load font
   font = draw_utils.font_with_size(24)
   
   # Measure text
   width, height = draw_utils.size_of_text("Hello", font)
   
   # Center text
   x, y = draw_utils.origin_to_center_text("Hello", font, 250, 122)

Configuration
~~~~~~~~~~~~~

.. code-block:: python

   from pykitmoney.resources import settings, secrets
   
   # Get settings
   child_name = settings.name()
   
   # Get access token
   token = secrets.access_token()

Complete API Reference
----------------------

See :doc:`api/modules` for complete API documentation with all functions,
parameters, and return values.
