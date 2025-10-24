"""Tests for Starling API modules."""

import pytest
from unittest.mock import patch, MagicMock
from pykitmoney.starling import accounts, feed, base_api


class TestBaseApi:
    """Tests for base_api module."""

    @patch("pykitmoney.starling.base_api.requests.get")
    def test_get_success(self, mock_get):
        """Test successful GET request."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"data": "test"}
        mock_get.return_value = mock_response

        result = base_api.get("test-token", "/api/v2/test")

        assert result == {"data": "test"}
        mock_get.assert_called_once()

    @patch("pykitmoney.starling.base_api.requests.get")
    def test_get_failure(self, mock_get):
        """Test failed GET request."""
        mock_response = MagicMock()
        mock_response.status_code = 401
        mock_get.return_value = mock_response

        result = base_api.get("test-token", "/api/v2/test")

        assert result is None

    @patch("pykitmoney.starling.base_api.requests.get")
    def test_get_with_query_params(self, mock_get):
        """Test GET request with query parameters."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"data": "test"}
        mock_get.return_value = mock_response

        query_params = {"param1": "value1"}
        result = base_api.get("test-token", "/api/v2/test", query_params)

        assert result == {"data": "test"}
        call_args = mock_get.call_args
        assert call_args[1]["params"] == query_params


class TestAccounts:
    """Tests for accounts module."""

    @patch("pykitmoney.starling.accounts.get")
    def test_get_accounts(self, mock_get):
        """Test getting accounts."""
        mock_get.return_value = {"accounts": [{"accountUid": "test-uid"}]}

        result = accounts.get_accounts("test-token")

        assert result == {"accounts": [{"accountUid": "test-uid"}]}
        mock_get.assert_called_once_with("test-token", "/api/v2/accounts")

    @patch("pykitmoney.starling.accounts.get")
    def test_get_spaces(self, mock_get):
        """Test getting spaces."""
        mock_get.return_value = {"spendingSpaces": []}

        result = accounts.get_spaces("test-token", "account-123")

        assert result == {"spendingSpaces": []}
        mock_get.assert_called_once()
        call_args = mock_get.call_args[0]
        assert "account-123" in call_args[1]

    @patch("pykitmoney.starling.accounts.get")
    def test_get_recurring_transfer(self, mock_get):
        """Test getting recurring transfer."""
        mock_get.return_value = {"currencyAndAmount": {"minorUnits": 1000}}

        result = accounts.get_recurring_transfer("test-token", "account-123", "space-456")

        assert result == {"currencyAndAmount": {"minorUnits": 1000}}
        mock_get.assert_called_once()


class TestFeed:
    """Tests for feed module."""

    @patch("pykitmoney.starling.feed.get")
    def test_get_transactions_for_category(self, mock_get):
        """Test getting transactions for a category."""
        mock_get.return_value = {"feedItems": []}

        result = feed.get_transactions_for_category("test-token", "account-123", "category-456")

        assert result == {"feedItems": []}
        mock_get.assert_called_once()
        call_args = mock_get.call_args
        assert "account-123" in call_args[0][1]
        assert "category-456" in call_args[0][1]
        assert call_args[0][2] is not None  # query_items should be present

    def test_three_months_ago_format(self):
        """Test three_months_ago returns valid ISO 8601 string."""
        result = feed.three_months_ago()

        # Should be a string in ISO 8601 format
        assert isinstance(result, str)
        assert "T" in result  # ISO 8601 has T separator
        # Should contain timezone info (+ or -)
        assert "+" in result or "-" in result.split("T")[1]
