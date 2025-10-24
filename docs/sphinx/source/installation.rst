Installation Guide
==================

This guide walks you through installing PyKitMoney on a Raspberry Pi Zero.

Hardware Requirements
---------------------

* Raspberry Pi Zero WH or Raspberry Pi Zero 2
* Waveshare 2.13" E-Paper HAT+ (250x122 pixels)
* MicroSD card (8GB or larger)
* Raspberry Pi Zero power supply
* Optional: Down-angle micro USB adapter

Software Requirements
---------------------

* Raspberry Pi OS (32-bit or 64-bit depending on your Pi)
* Python 3.9 or newer
* Git
* SPI enabled on the Raspberry Pi

Step-by-Step Installation
--------------------------

1. Set Up Raspberry Pi OS
~~~~~~~~~~~~~~~~~~~~~~~~~~

Use Raspberry Pi Imager to flash the SD card:

.. code-block:: bash

   # Download from https://www.raspberrypi.com/software/
   # Select Raspberry Pi OS (not Lite version)
   # Configure hostname, WiFi, SSH in advanced settings

2. Enable SPI Interface
~~~~~~~~~~~~~~~~~~~~~~~

The e-paper display requires SPI to be enabled:

.. code-block:: bash

   sudo raspi-config
   # Navigate to: Interfacing Options > SPI > Yes

3. Install System Dependencies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Update your system and install required packages:

.. code-block:: bash

   sudo apt-get update
   sudo apt-get upgrade
   sudo apt install git python3-venv python3-pip

4. Clone the Repository
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   git clone https://github.com/AaronTunney/PyKitMoney.git
   cd PyKitMoney

5. Create Virtual Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   python3 -m venv .venv
   source .venv/bin/activate

6. Install PyKitMoney
~~~~~~~~~~~~~~~~~~~~~

For Raspberry Pi with e-paper display:

.. code-block:: bash

   pip install -e ".[pi]"

For development (without hardware dependencies):

.. code-block:: bash

   pip install -e ".[dev]"

7. Configure Your Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~

See the :doc:`configuration` guide for setting up your API tokens and preferences.

8. Test the Installation
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   pykitmoney

If configured correctly, your e-paper display should update with account information.

Verification
------------

Check that the installation was successful:

.. code-block:: bash

   # Verify the command is available
   which pykitmoney

   # Run the test suite
   pytest

   # Check Python version
   python --version  # Should be 3.9 or newer

Next Steps
----------

* :doc:`configuration` - Set up your Starling Bank API access
* :doc:`usage` - Learn how to use PyKitMoney
* :doc:`troubleshooting` - Common issues and solutions
