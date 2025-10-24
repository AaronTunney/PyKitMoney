Development Guide
=================

This guide is for developers who want to modify or extend PyKitMoney.

Setting Up Development Environment
-----------------------------------

Clone and Install
~~~~~~~~~~~~~~~~~

.. code-block:: bash

   git clone https://github.com/AaronTunney/PyKitMoney.git
   cd PyKitMoney
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -e ".[dev]"

This installs PyKitMoney in editable mode with development dependencies:

* pytest - Testing framework
* pytest-cov - Coverage reporting
* black - Code formatter
* pylint - Linter
* mypy - Type checker
* sphinx - Documentation generator

Project Structure
-----------------

.. code-block:: text

   PyKitMoney/
   ├── pykitmoney/              # Main package
   │   ├── __init__.py         # Package initialization
   │   ├── main.py             # Entry point
   │   ├── utils.py            # Utility functions
   │   ├── draw_utils.py       # Drawing utilities
   │   ├── epaper_drawing.py   # E-paper display logic
   │   ├── starling/           # Starling Bank API
   │   │   ├── accounts.py     # Account/space APIs
   │   │   ├── feed.py         # Transaction feed
   │   │   └── base_api.py     # HTTP client
   │   ├── resources/          # Configuration
   │   │   ├── secrets.py      # Token management
   │   │   └── settings.py     # Settings management
   │   └── pic/                # Font resources
   ├── tests/                  # Test suite
   │   ├── test_utils.py
   │   ├── test_starling.py
   │   └── test_draw_utils.py
   ├── docs/                   # Documentation
   │   ├── sphinx/            # Sphinx docs
   │   └── API.md             # API reference
   ├── service/                # Systemd files
   └── pyproject.toml          # Package configuration

Code Style
----------

Black Formatting
~~~~~~~~~~~~~~~~

Format code before committing:

.. code-block:: bash

   black pykitmoney tests

Check without modifying:

.. code-block:: bash

   black --check pykitmoney tests

Configuration is in ``pyproject.toml``:

* Line length: 100 characters
* Target: Python 3.9+

Linting
~~~~~~~

Run Pylint:

.. code-block:: bash

   pylint pykitmoney

Configuration is in ``pyproject.toml``.

Type Checking
~~~~~~~~~~~~~

Run MyPy (optional):

.. code-block:: bash

   mypy pykitmoney

Testing
-------

See :doc:`testing` for comprehensive testing guide.

Quick test:

.. code-block:: bash

   pytest

With coverage:

.. code-block:: bash

   pytest --cov=pykitmoney --cov-report=html

Documentation
-------------

Building Docs
~~~~~~~~~~~~~

Build Sphinx documentation:

.. code-block:: bash

   cd docs/sphinx
   make html
   # Open build/html/index.html

Docstring Format
~~~~~~~~~~~~~~~~

Use Google-style docstrings:

.. code-block:: python

   def example_function(param1, param2):
       """
       Brief description.
       
       Longer description if needed.
       
       Args:
           param1: Description of param1.
           param2: Description of param2.
           
       Returns:
           Description of return value.
           
       Raises:
           ValueError: When param1 is invalid.
       """
       pass

Module Architecture
-------------------

Main Entry Point
~~~~~~~~~~~~~~~~

``pykitmoney/main.py``:

* Configures logging
* Loads configuration
* Fetches data from Starling API
* Formats display data
* Updates e-paper display

Starling API Client
~~~~~~~~~~~~~~~~~~~

``pykitmoney/starling/``:

* ``base_api.py``: HTTP GET wrapper
* ``accounts.py``: Account and space endpoints
* ``feed.py``: Transaction feed endpoints

Each API function:

1. Takes access token as parameter
2. Constructs endpoint URL
3. Makes GET request
4. Returns parsed JSON or None

Display Rendering
~~~~~~~~~~~~~~~~~

``pykitmoney/epaper_drawing.py``:

* Only imported on Raspberry Pi
* Uses waveshare-epaper library
* Draws to PIL Image
* Transfers to display

``pykitmoney/draw_utils.py``:

* Font loading and sizing
* Text measurement
* Layout calculations
* Platform-independent

Utilities
~~~~~~~~~

``pykitmoney/utils.py``:

* Data extraction helpers
* Currency formatting
* Date parsing
* Platform detection

Adding Features
---------------

Adding a New API Endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Add function to appropriate module in ``starling/``:

   .. code-block:: python

      def get_new_endpoint(access_token, param):
          """Get data from new endpoint."""
          endpoint = f"/api/v2/new/{param}"
          return get(access_token, endpoint)

2. Add tests in ``tests/test_starling.py``

3. Document in ``docs/API.md``

Modifying Display Layout
~~~~~~~~~~~~~~~~~~~~~~~~~

Edit ``pykitmoney/epaper_drawing.py``:

* Adjust positions in ``draw_to_epaper_display()``
* Use ``draw_utils`` for calculations
* Test on actual hardware

Remember: E-paper is 250x122 pixels

Adding Configuration Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Add to ``resources/settings.json``:

   .. code-block:: json

      {
          "name": "Kate",
          "new_option": "value"
      }

2. Add getter to ``resources/settings.py``:

   .. code-block:: python

      def new_option():
          """Get new option value."""
          return settings().get('new_option')

3. Use in your code:

   .. code-block:: python

      from pykitmoney.resources import settings
      value = settings.new_option()

Git Workflow
------------

Branching
~~~~~~~~~

* ``main`` - Stable releases
* ``develop`` - Active development
* Feature branches: ``feature/description``
* Bug fixes: ``fix/description``

Commits
~~~~~~~

Use conventional commit messages:

.. code-block:: text

   type(scope): subject

   body (optional)

   footer (optional)

Types:

* ``feat``: New feature
* ``fix``: Bug fix
* ``docs``: Documentation
* ``style``: Formatting
* ``refactor``: Code restructuring
* ``test``: Tests
* ``chore``: Maintenance

Example:

.. code-block:: text

   feat(display): add transaction category icons
   
   Adds small icons next to transactions based on category.
   
   Closes #42

Pull Requests
~~~~~~~~~~~~~

Before submitting:

1. Run tests: ``pytest``
2. Format code: ``black pykitmoney tests``
3. Update documentation
4. Add tests for new features
5. Update CHANGELOG.md

Debugging
---------

Without Hardware
~~~~~~~~~~~~~~~~

Develop most features without Raspberry Pi:

.. code-block:: bash

   pip install -e ".[dev]"  # Omits hardware dependencies

Mock the display in tests:

.. code-block:: python

   from unittest.mock import patch
   
   @patch('pykitmoney.utils.is_raspberry_pi')
   def test_something(mock_is_pi):
       mock_is_pi.return_value = False
       # Your test

With Hardware
~~~~~~~~~~~~~

Connect via SSH and run manually:

.. code-block:: bash

   source .venv/bin/activate
   python -m pykitmoney.main

Add debug logging:

.. code-block:: python

   import logging
   logging.basicConfig(level=logging.DEBUG)

Performance Considerations
--------------------------

* E-paper updates are slow (5-10 seconds)
* API calls add latency (1-3 seconds each)
* Minimize display refreshes
* Cache data when possible
* Use timers, not continuous polling

Security Considerations
-----------------------

* Never commit access tokens
* Use read-only API scopes
* Validate all external data
* No user input accepted
* Runs as non-root user

Release Process
---------------

1. Update version in ``pyproject.toml``
2. Update ``CHANGELOG.md``
3. Run full test suite
4. Build documentation
5. Create git tag: ``v1.0.0``
6. Push to GitHub
7. Create GitHub release

Resources
---------

* Starling API Docs: https://developer.starlingbank.com/docs
* Waveshare Wiki: https://www.waveshare.com/wiki/2.13inch_e-Paper_HAT
* Python Packaging: https://packaging.python.org/
* Pytest Docs: https://docs.pytest.org/

Next Steps
----------

* :doc:`testing` - Write and run tests
* :doc:`contributing` - Contribution guidelines
* :doc:`api` - API reference
