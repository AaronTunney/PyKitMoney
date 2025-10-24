Usage Guide
===========

This guide explains how to run and use PyKitMoney.

Running PyKitMoney
------------------

Manual Execution
~~~~~~~~~~~~~~~~

Activate the virtual environment and run:

.. code-block:: bash

   source .venv/bin/activate
   pykitmoney

Alternative methods:

.. code-block:: bash

   # Using module execution
   python -m pykitmoney.main
   
   # Direct execution
   python pykitmoney/main.py

The display will update with:

* Child's name (top left)
* Current balance (bottom left, large text)
* Next pocket money transfer (top right)
* Last 3 transactions (bottom right)

Setting Up Automatic Updates
-----------------------------

Use systemd to run PyKitMoney automatically.

Step 1: Configure Service File
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Edit ``service/pykitmoney.service`` and update the path:

.. code-block:: ini

   [Service]
   Type=oneshot
   ExecStart=/home/youruser/PyKitMoney/.venv/bin/python3 -m pykitmoney.main

Replace ``/home/youruser/PyKitMoney`` with your actual project path.

Step 2: Install Service
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   sudo cp service/pykitmoney.* /etc/systemd/system/
   sudo systemctl daemon-reload

Step 3: Enable and Start
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Start the service
   sudo systemctl start pykitmoney
   
   # Enable at boot
   sudo systemctl enable pykitmoney
   
   # Enable the timer (hourly updates)
   sudo systemctl enable pykitmoney.timer
   sudo systemctl start pykitmoney.timer

Step 4: Verify Status
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Check service status
   sudo systemctl status pykitmoney
   
   # Check timer status
   sudo systemctl list-timers pykitmoney.timer
   
   # View recent logs
   sudo journalctl -u pykitmoney.service -n 50

Understanding the Display
-------------------------

Layout
~~~~~~

The 250x122 pixel display is divided into four sections:

.. code-block:: text

   +----------------+----------------+
   | Child's Name   | Next: £5.00    |
   +----------------+----------------+
   |                | 15 Jan -£2.50  |
   |    £47.23      | 14 Jan +£5.00  |
   |                | 12 Jan -£3.00  |
   +----------------+----------------+

Sections:

* **Top Left**: Child's name from settings.json
* **Bottom Left**: Current balance (largest text)
* **Top Right**: Next scheduled transfer amount
* **Bottom Right**: Last 3 transactions (date and amount)

Transaction Display
~~~~~~~~~~~~~~~~~~~

Transactions show:

* Date (day and month)
* Direction (+ for incoming, - for outgoing)
* Amount in £

Example: ``15 Jan -£2.50`` means £2.50 spent on January 15th.

Update Behavior
~~~~~~~~~~~~~~~

* E-paper displays persist without power
* Updates only occur when the script runs
* Default: hourly updates via systemd timer
* No flashing/flickering between updates

Command Options
---------------

PyKitMoney has no command-line options. Configuration is done via:

* ``resources/settings.json`` - Runtime settings
* ``resources/accesstoken.txt`` - API authentication

Environment Variables
---------------------

None currently used. All configuration is file-based.

Logs and Debugging
------------------

View Logs
~~~~~~~~~

When running manually:

.. code-block:: bash

   pykitmoney

Logs are printed to stdout with timestamps.

When running via systemd:

.. code-block:: bash

   # Recent logs
   sudo journalctl -u pykitmoney.service -n 50
   
   # Follow logs in real-time
   sudo journalctl -u pykitmoney.service -f
   
   # Today's logs
   sudo journalctl -u pykitmoney.service --since today

Log Levels
~~~~~~~~~~

PyKitMoney logs at INFO level by default:

* INFO: Normal operations (API calls, display updates)
* WARNING: Non-critical issues (empty data)
* ERROR: Problems that prevent operation

Stopping Automatic Updates
---------------------------

Temporarily stop:

.. code-block:: bash

   sudo systemctl stop pykitmoney.timer

Disable permanently:

.. code-block:: bash

   sudo systemctl disable pykitmoney.timer
   sudo systemctl stop pykitmoney.timer

Manual Update Trigger
~~~~~~~~~~~~~~~~~~~~~

Force an immediate update:

.. code-block:: bash

   sudo systemctl start pykitmoney

Power Consumption
-----------------

* E-paper displays use power only during updates
* Raspberry Pi Zero: ~100-150mA idle
* During update: brief spike to ~200mA
* Can run 24/7 on standard power supply

Display Lifespan
----------------

E-paper displays have a limited number of refresh cycles:

* Typical: 100,000+ refreshes
* At hourly updates: ~11 years
* At daily updates: ~274 years

Next Steps
----------

* :doc:`troubleshooting` - Solve common issues
* :doc:`development` - Modify or extend PyKitMoney
