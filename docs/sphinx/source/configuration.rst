Configuration Guide
===================

This guide explains how to configure PyKitMoney for your Starling Kite account.

Overview
--------

PyKitMoney requires two pieces of configuration:

1. Your child's name (used to find their Kite space)
2. A Starling Bank API access token (for read-only access)

Creating a Starling Developer Account
--------------------------------------

Step 1: Access Developer Portal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Visit https://developer.starlingbank.com/
2. Sign in with your Starling Bank credentials
3. Navigate to "Personal Access"

Step 2: Generate Access Token
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a new personal access token with the following scopes:

* ``account:read`` - Read account information
* ``account-list:read`` - List all accounts  
* ``savings-goal-transfer:read`` - Read recurring transfers
* ``space:read`` - Read space information
* ``transaction:read`` - Read transaction feed

.. warning::
   **Do not grant any write permissions!** Only read permissions are needed.
   The access token gives access to your real bank account.

Step 3: Copy Your Token
~~~~~~~~~~~~~~~~~~~~~~~~

Copy the generated access token. You'll need it for the next step.

Configuring PyKitMoney
-----------------------

Create Configuration Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~

From the project root directory:

.. code-block:: bash

   cp resources/settings.json.example resources/settings.json
   cp resources/accesstoken.txt.example resources/accesstoken.txt

Edit Settings File
~~~~~~~~~~~~~~~~~~

Edit ``resources/settings.json``:

.. code-block:: json

   {
       "name": "YourChildName"
   }

Replace ``YourChildName`` with the name of your child's Kite space 
(exactly as it appears in the Starling app).

Add Access Token
~~~~~~~~~~~~~~~~

Edit ``resources/accesstoken.txt`` and paste your access token:

.. code-block:: text

   eyJhbGciOiJQUzI1NiIsInppcCI6Ik...  (your token)

Save the file with just the token, no extra spaces or newlines.

File Locations
--------------

Configuration files are located in the ``resources/`` directory:

.. code-block:: text

   PyKitMoney/
   └── resources/
       ├── settings.json       # Your child's name
       └── accesstoken.txt     # Starling API token

.. note::
   These files are excluded from version control via ``.gitignore`` 
   to protect your sensitive information.

Display Configuration
---------------------

E-Paper Display Model
~~~~~~~~~~~~~~~~~~~~~

If you have a different version of the Waveshare 2.13" display, 
edit ``pykitmoney/epaper_drawing.py``:

.. code-block:: python

   # Line 18
   epd = epaper.epaper('epd2in13_V3').EPD()
   
   # Change 'epd2in13_V3' to your model:
   # - 'epd2in13_V2' for Version 2
   # - 'epd2in13_V4' for Version 4
   # etc.

Update Frequency
~~~~~~~~~~~~~~~~

The default update frequency is hourly. To change this, edit ``service/pykitmoney.timer``:

.. code-block:: ini

   [Timer]
   OnBootSec=1min
   OnUnitActiveSec=1h  # Change to desired frequency

Verifying Configuration
-----------------------

Test your configuration:

.. code-block:: bash

   source .venv/bin/activate
   pykitmoney

You should see:

* Log messages showing API calls
* Your child's name on the display
* Current balance
* Recent transactions
* Next scheduled transfer

If you see errors, check:

* Token is correct and has not expired
* Child's name matches exactly (case-sensitive)
* SPI is enabled on Raspberry Pi
* Network connectivity is working

Security Best Practices
-----------------------

* **Never commit** ``accesstoken.txt`` to version control
* **Use read-only scopes** - no write permissions needed
* **Regenerate tokens** if you suspect they've been compromised
* **Restrict access** to the Raspberry Pi (change default passwords)
* **Keep the system updated** with security patches

Next Steps
----------

* :doc:`usage` - Run PyKitMoney and set up automatic updates
* :doc:`troubleshooting` - Solve common configuration issues
