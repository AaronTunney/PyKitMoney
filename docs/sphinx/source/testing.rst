Testing Guide
=============

PyKitMoney has a comprehensive test suite using pytest.

Running Tests
-------------

Basic Test Run
~~~~~~~~~~~~~~

.. code-block:: bash

   pytest

Verbose Output
~~~~~~~~~~~~~~

.. code-block:: bash

   pytest -v

With Coverage
~~~~~~~~~~~~~

.. code-block:: bash

   pytest --cov=pykitmoney --cov-report=html
   # Open htmlcov/index.html

Specific Tests
~~~~~~~~~~~~~~

.. code-block:: bash

   # Run specific file
   pytest tests/test_utils.py
   
   # Run specific test
   pytest tests/test_utils.py::TestCurrencyString::test_currency_string_formatting
   
   # Run tests matching pattern
   pytest -k "currency"

Test Organization
-----------------

Tests are organized by module:

* ``tests/test_utils.py`` - Utility function tests
* ``tests/test_starling.py`` - API client tests
* ``tests/test_draw_utils.py`` - Drawing utility tests

Each test file contains test classes grouping related tests:

.. code-block:: python

   class TestCurrencyString:
       """Tests for currency_string function."""
       
       def test_currency_string_formatting(self):
           """Test currency formatting."""
           result = utils.currency_string(1234)
           assert '12' in result

Writing Tests
-------------

Test Structure
~~~~~~~~~~~~~~

Use pytest conventions:

* Test files: ``test_*.py``
* Test classes: ``Test*``
* Test functions: ``test_*``

Example:

.. code-block:: python

   import pytest
   from pykitmoney import utils

   class TestMyFunction:
       """Tests for my_function."""
       
       def test_basic_case(self):
           """Test basic functionality."""
           result = utils.my_function("input")
           assert result == "expected"
       
       def test_edge_case(self):
           """Test edge case."""
           with pytest.raises(ValueError):
               utils.my_function("")

Mocking
~~~~~~~

Use unittest.mock for external dependencies:

.. code-block:: python

   from unittest.mock import patch, MagicMock
   
   @patch('pykitmoney.starling.base_api.requests.get')
   def test_api_call(mock_get):
       """Test API call."""
       mock_response = MagicMock()
       mock_response.status_code = 200
       mock_response.json.return_value = {'data': 'test'}
       mock_get.return_value = mock_response
       
       result = base_api.get('token', '/endpoint')
       assert result == {'data': 'test'}

Fixtures
~~~~~~~~

Use pytest fixtures for reusable test data:

.. code-block:: python

   import pytest
   
   @pytest.fixture
   def sample_accounts():
       """Sample accounts data."""
       return {
           'accounts': [
               {'accountUid': 'abc-123'}
           ]
       }
   
   def test_find_account(sample_accounts):
       """Test with fixture."""
       uid = utils.find_first_account_uid(sample_accounts)
       assert uid == 'abc-123'

Coverage Goals
--------------

Target coverage levels:

* Overall: 80%+
* Core modules (utils, starling): 95%+
* Display modules: 60%+ (hardware-dependent)

View coverage report:

.. code-block:: bash

   pytest --cov=pykitmoney --cov-report=term-missing

Continuous Integration
----------------------

Tests run automatically on:

* Push to main/develop branches
* Pull requests
* Multiple Python versions (3.9-3.12)

See ``.github/workflows/tests.yml`` for CI configuration.

Testing Best Practices
----------------------

1. **Test one thing per test**: Each test should verify one behavior
2. **Use descriptive names**: ``test_currency_string_with_zero``
3. **Test edge cases**: Empty inputs, None, negative numbers
4. **Mock external dependencies**: API calls, file I/O, hardware
5. **Keep tests fast**: Use mocks, avoid slow operations
6. **Test error cases**: Verify exceptions are raised properly
7. **Use assertions clearly**: Make failures obvious

Test Examples
-------------

Testing Utility Functions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   def test_find_spending_space():
       """Test finding a space that exists."""
       spaces = {
           'spendingSpaces': [
               {'name': 'Alice', 'balance': {'minorUnits': 1000}}
           ]
       }
       result = utils.find_spending_space('Alice', spaces)
       assert result is not None
       assert result['name'] == 'Alice'

Testing API Calls
~~~~~~~~~~~~~~~~~

.. code-block:: python

   @patch('pykitmoney.starling.accounts.get')
   def test_get_accounts(mock_get):
       """Test getting accounts."""
       mock_get.return_value = {'accounts': []}
       result = accounts.get_accounts('token')
       assert result == {'accounts': []}
       mock_get.assert_called_once_with('token', '/api/v2/accounts')

Testing Exceptions
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   def test_invalid_input():
       """Test function raises error on invalid input."""
       with pytest.raises(ValueError) as exc_info:
           utils.some_function(invalid_value)
       assert "Invalid" in str(exc_info.value)

Debugging Tests
---------------

Run with output:

.. code-block:: bash

   pytest -s  # Show print statements

Run with debugger:

.. code-block:: bash

   pytest --pdb  # Drop into debugger on failure

Show local variables:

.. code-block:: bash

   pytest -l  # Show locals in tracebacks

Next Steps
----------

* :doc:`development` - Development workflow
* :doc:`contributing` - Contribution guidelines
