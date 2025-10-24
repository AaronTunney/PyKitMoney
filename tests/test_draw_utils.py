"""Tests for drawing utilities."""

import pytest
from unittest.mock import MagicMock, patch
from PIL import ImageFont
from pykitmoney import draw_utils


class TestSizeOfText:
    """Tests for size_of_text function."""

    @patch("pykitmoney.draw_utils.font_with_size")
    def test_size_of_text_returns_tuple(self, mock_font):
        """Test that size_of_text returns a tuple."""
        mock_font_obj = MagicMock()
        mock_font_obj.getmetrics.return_value = (10, 3)
        mock_mask = MagicMock()
        mock_mask.getbbox.return_value = (0, 0, 50, 10)
        mock_font_obj.getmask.return_value = mock_mask

        result = draw_utils.size_of_text("Test", mock_font_obj)

        assert isinstance(result, tuple)
        assert len(result) == 2
        assert isinstance(result[0], int)
        assert isinstance(result[1], int)


class TestOriginToCenterText:
    """Tests for origin_to_center_text function."""

    @patch("pykitmoney.draw_utils.size_of_text")
    def test_center_text_in_square(self, mock_size):
        """Test centering text in a square."""
        mock_size.return_value = (50, 20)
        mock_font = MagicMock()

        result = draw_utils.origin_to_center_text("Test", mock_font, 100, 100)

        assert isinstance(result, tuple)
        assert len(result) == 2
        # Should center horizontally and vertically
        assert result[0] == 25  # (100 - 50) / 2
        assert result[1] == 40  # (100 - 20) / 2


class TestLongestText:
    """Tests for longest_text function."""

    @patch("pykitmoney.draw_utils.size_of_text")
    def test_longest_text_selection(self, mock_size):
        """Test selecting the longest text."""
        mock_font = MagicMock()
        mock_size.side_effect = [(30, 10), (50, 10), (40, 10)]

        texts = ["Short", "Longer text", "Medium"]
        result = draw_utils.longest_text(texts, mock_font)

        assert result == "Longer text"
