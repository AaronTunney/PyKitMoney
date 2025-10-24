"""Tests for utility functions."""

import pytest
from unittest.mock import patch, mock_open
from pykitmoney import utils


class TestFindSpendingSpace:
    """Tests for find_spending_space function."""

    def test_find_existing_space(self):
        """Test finding a space that exists."""
        spaces = {
            "spendingSpaces": [
                {"name": "Alice", "balance": {"minorUnits": 1000}},
                {"name": "Bob", "balance": {"minorUnits": 2000}},
            ]
        }
        result = utils.find_spending_space("Alice", spaces)
        assert result is not None
        assert result["name"] == "Alice"
        assert result["balance"]["minorUnits"] == 1000

    def test_find_nonexistent_space(self):
        """Test finding a space that doesn't exist."""
        spaces = {"spendingSpaces": [{"name": "Alice", "balance": {"minorUnits": 1000}}]}
        result = utils.find_spending_space("Charlie", spaces)
        assert result is None


class TestFindSavingSpace:
    """Tests for find_saving_space function."""

    def test_find_existing_saving_space(self):
        """Test finding a saving space that exists."""
        spaces = {
            "savingsGoals": [
                {"name": "Holiday", "totalSaved": {"minorUnits": 5000}},
                {"name": "Bike", "totalSaved": {"minorUnits": 3000}},
            ]
        }
        result = utils.find_saving_space("Holiday", spaces)
        assert result is not None
        assert result["name"] == "Holiday"

    def test_find_nonexistent_saving_space(self):
        """Test finding a saving space that doesn't exist."""
        spaces = {"savingsGoals": [{"name": "Holiday", "totalSaved": {"minorUnits": 5000}}]}
        result = utils.find_saving_space("Car", spaces)
        assert result is None


class TestFindFirstAccountUid:
    """Tests for find_first_account_uid function."""

    def test_find_account_uid_with_accounts(self):
        """Test finding account UID when accounts exist."""
        accounts_data = {
            "accounts": [
                {"accountUid": "abc-123", "name": "Main Account"},
                {"accountUid": "def-456", "name": "Savings Account"},
            ]
        }
        result = utils.find_first_account_uid(accounts_data)
        assert result == "abc-123"

    def test_find_account_uid_no_accounts(self):
        """Test finding account UID when no accounts exist."""
        accounts_data = {"accounts": []}
        result = utils.find_first_account_uid(accounts_data)
        assert result is None


class TestCurrencyString:
    """Tests for currency_string function."""

    @patch("pykitmoney.utils.is_raspberry_pi")
    def test_currency_string_formatting(self, mock_is_pi):
        """Test currency formatting."""
        mock_is_pi.return_value = False
        result = utils.currency_string(1234)
        # Result should be a currency string (format varies by locale)
        assert "12" in result
        assert "34" in result or ".34" in result

    @patch("pykitmoney.utils.is_raspberry_pi")
    def test_currency_string_zero(self, mock_is_pi):
        """Test currency formatting for zero."""
        mock_is_pi.return_value = False
        result = utils.currency_string(0)
        assert "0" in result


class TestIsRaspberryPi:
    """Tests for is_raspberry_pi function."""

    @patch("pykitmoney.utils.io.open", mock_open(read_data="Raspberry Pi Zero"))
    def test_is_raspberry_pi_true(self):
        """Test detecting Raspberry Pi."""
        result = utils.is_raspberry_pi()
        assert result is True

    @patch("pykitmoney.utils.io.open", side_effect=FileNotFoundError)
    def test_is_raspberry_pi_false(self, mock_file):
        """Test detecting non-Raspberry Pi."""
        result = utils.is_raspberry_pi()
        assert result is False


class TestDateFromIso8601String:
    """Tests for date_from_iso_8601_string function."""

    def test_parse_valid_iso_date(self):
        """Test parsing valid ISO 8601 date."""
        date_str = "2024-01-15T10:30:00+00:00"
        result = utils.date_from_iso_8601_string(date_str)
        assert result.year == 2024
        assert result.month == 1
        assert result.day == 15
        assert result.hour == 10
        assert result.minute == 30

    def test_parse_iso_date_without_timezone(self):
        """Test parsing ISO 8601 date without timezone."""
        date_str = "2024-01-15T10:30:00"
        result = utils.date_from_iso_8601_string(date_str)
        assert result.year == 2024
        assert result.month == 1
        assert result.day == 15
