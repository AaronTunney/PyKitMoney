Troubleshooting
===============

Common issues and their solutions.

Display Issues
--------------

Display Not Updating
~~~~~~~~~~~~~~~~~~~~

**Symptom**: E-paper display shows nothing or old data.

**Solutions**:

1. Check SPI is enabled:

   .. code-block:: bash

      sudo raspi-config
      # Interfacing Options > SPI > Enable

2. Verify the display model in code:

   .. code-block:: python

      # pykitmoney/epaper_drawing.py, line 18
      epd = epaper.epaper('epd2in13_V3').EPD()

3. Check GPIO permissions:

   .. code-block:: bash

      # Add user to gpio group
      sudo usermod -a -G gpio $USER
      # Reboot
      sudo reboot

4. Test with waveshare example:

   .. code-block:: bash

      # Try the waveshare library examples
      python -m epaper.examples.epd2in13_V3_test

Display Shows Garbage
~~~~~~~~~~~~~~~~~~~~~

**Symptom**: Random pixels or corrupted image.

**Solutions**:

* Power cycle the Raspberry Pi
* Check ribbon cable connection
* Verify display is compatible (V3 recommended)
* Try a different power supply (needs stable 5V)

API and Authentication
----------------------

401 Unauthorized Error
~~~~~~~~~~~~~~~~~~~~~~

**Symptom**: ``Request failed with status code 401``

**Solutions**:

1. Verify access token:

   .. code-block:: bash

      cat resources/accesstoken.txt
      # Should be single line, no spaces

2. Check token hasn't expired:

   * Log in to Starling Developer Portal
   * Verify token status
   * Regenerate if needed

3. Verify token permissions include all required scopes

404 Not Found Error
~~~~~~~~~~~~~~~~~~~

**Symptom**: Account or space not found.

**Solutions**:

1. Check child's name matches exactly:

   .. code-block:: json

      {
          "name": "Kate"  // Must match Starling app exactly
      }

2. Verify Kite space exists in Starling app

3. Check account is accessible with token

No Transactions Showing
~~~~~~~~~~~~~~~~~~~~~~~

**Symptom**: Balance shows but no transactions.

**Possible causes**:

* No transactions in last 3 months
* Kite space has never been used
* API permissions insufficient

Check logs for details:

.. code-block:: bash

   sudo journalctl -u pykitmoney.service -n 100

Network Issues
--------------

Cannot Connect to API
~~~~~~~~~~~~~~~~~~~~~

**Symptom**: ``Request error: ...`` or timeout errors.

**Solutions**:

1. Test network connectivity:

   .. code-block:: bash

      ping -c 4 api.starlingbank.com

2. Check DNS resolution:

   .. code-block:: bash

      nslookup api.starlingbank.com

3. Verify WiFi is connected:

   .. code-block:: bash

      iwconfig wlan0

4. Test with curl:

   .. code-block:: bash

      curl -H "Authorization: Bearer YOUR_TOKEN" \
           https://api.starlingbank.com/api/v2/accounts

Slow Updates
~~~~~~~~~~~~

**Symptom**: Updates take long time.

**Normal behavior**: E-paper refresh takes 5-10 seconds

If longer:

* Check network speed
* Verify Pi isn't throttling (temperature)
* Check system load

Systemd Service Issues
-----------------------

Service Won't Start
~~~~~~~~~~~~~~~~~~~

**Symptom**: ``systemctl status pykitmoney`` shows failed.

**Solutions**:

1. Check logs:

   .. code-block:: bash

      sudo journalctl -u pykitmoney.service -n 50

2. Verify paths in service file:

   .. code-block:: bash

      sudo nano /etc/systemd/system/pykitmoney.service
      # Check ExecStart path is correct

3. Test manual execution:

   .. code-block:: bash

      cd /path/to/PyKitMoney
      source .venv/bin/activate
      pykitmoney

4. Reload systemd:

   .. code-block:: bash

      sudo systemctl daemon-reload
      sudo systemctl restart pykitmoney

Timer Not Running
~~~~~~~~~~~~~~~~~

**Symptom**: No automatic updates.

**Solutions**:

1. Check timer status:

   .. code-block:: bash

      systemctl list-timers pykitmoney.timer

2. Verify timer is enabled:

   .. code-block:: bash

      sudo systemctl enable pykitmoney.timer
      sudo systemctl start pykitmoney.timer

3. Check timer configuration:

   .. code-block:: bash

      systemctl cat pykitmoney.timer

Permission Denied
~~~~~~~~~~~~~~~~~

**Symptom**: Service fails with permission errors.

**Solutions**:

* Verify virtual environment ownership
* Check file permissions in project directory
* Ensure user in service file exists

Installation Problems
---------------------

Module Not Found
~~~~~~~~~~~~~~~~

**Symptom**: ``ModuleNotFoundError: No module named 'pykitmoney'``

**Solutions**:

1. Reinstall package:

   .. code-block:: bash

      pip install -e ".[pi]"

2. Verify virtual environment:

   .. code-block:: bash

      which python
      # Should show .venv/bin/python

3. Check installation:

   .. code-block:: bash

      pip show pykitmoney

Dependencies Won't Install
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Symptom**: pip install fails.

**Solutions**:

1. Update pip:

   .. code-block:: bash

      pip install --upgrade pip

2. Install system dependencies:

   .. code-block:: bash

      sudo apt-get install python3-dev build-essential

3. For Pillow issues:

   .. code-block:: bash

      sudo apt-get install libjpeg-dev zlib1g-dev

Python Version Too Old
~~~~~~~~~~~~~~~~~~~~~~

**Symptom**: ``requires Python >=3.9``

**Solutions**:

* Use Raspberry Pi OS Bullseye or newer
* Or install Python 3.9+ from source (advanced)

Configuration Issues
--------------------

Settings Not Applied
~~~~~~~~~~~~~~~~~~~~

**Symptom**: Changes to settings.json ignored.

**Solutions**:

* Restart the service after changes
* Verify JSON syntax is valid
* Check no typos in key names

Token File Not Read
~~~~~~~~~~~~~~~~~~~

**Symptom**: Error reading accesstoken.txt.

**Solutions**:

1. Check file exists:

   .. code-block:: bash

      ls -la resources/accesstoken.txt

2. Verify no extra whitespace:

   .. code-block:: bash

      cat -A resources/accesstoken.txt
      # Should show: your-token$

3. Check file permissions:

   .. code-block:: bash

      chmod 600 resources/accesstoken.txt

Getting Help
------------

If you're still stuck:

1. **Check logs** thoroughly:

   .. code-block:: bash

      sudo journalctl -u pykitmoney.service --since "1 hour ago"

2. **Search GitHub Issues**: 
   https://github.com/AaronTunney/PyKitMoney/issues

3. **Open a new issue** with:
   
   * Full error message
   * Log output
   * Hardware/software versions
   * Steps to reproduce

4. **Review documentation**:
   
   * :doc:`installation` - Setup steps
   * :doc:`configuration` - Token and settings
   * :doc:`usage` - Running the application
