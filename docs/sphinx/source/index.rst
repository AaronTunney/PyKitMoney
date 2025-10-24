.. PyKitMoney documentation master file

PyKitMoney Documentation
========================

Display Starling Kite information on an e-paper display connected to a Raspberry Pi Zero.

.. image:: https://img.shields.io/badge/python-3.9+-blue.svg
   :target: https://www.python.org/downloads/
   :alt: Python 3.9+

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Code style: black

Overview
--------

PyKitMoney is a Python application that displays your child's Starling Kite account balance and 
recent transactions on a Waveshare 2.13" e-paper display connected to a Raspberry Pi Zero.

We live in an increasingly cashless society and, moving with the times, children now have digital 
bank accounts like Starling Kite rather than physical pocket money. This project solves the 
problem of checking balances without giving young children a smartphone.

Features
--------

* Display current balance in large, easy-to-read text
* Show the last 3 transactions
* Display next scheduled pocket money transfer
* Automatic hourly updates via systemd timer
* Minimal power consumption with e-paper display
* Secure read-only access to Starling Bank API

Quick Start
-----------

For Raspberry Pi Installation:

.. code-block:: bash

   git clone https://github.com/AaronTunney/PyKitMoney.git
   cd PyKitMoney
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -e ".[pi]"
   pykitmoney

For Development:

.. code-block:: bash

   pip install -e ".[dev]"
   pytest
   black pykitmoney tests

Table of Contents
-----------------

.. toctree::
   :maxdepth: 2
   :caption: User Guide

   installation
   configuration
   usage
   troubleshooting

.. toctree::
   :maxdepth: 2
   :caption: Developer Guide

   development
   testing
   api

.. toctree::
   :maxdepth: 2
   :caption: API Reference

   api/modules
   api/pykitmoney
   api/starling
   api/resources

.. toctree::
   :maxdepth: 1
   :caption: Additional Information

   GitHub Repository <https://github.com/AaronTunney/PyKitMoney>

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
