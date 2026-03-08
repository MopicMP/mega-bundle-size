"""Tests for mega-bundle-size."""

import os
import tempfile
import pytest
from mega_bundle_size import size


class TestSize:
    """Test suite for size."""

    def test_basic(self):
        """Test basic usage with a real temp directory."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create a sample file inside
            sample = os.path.join(tmpdir, "sample.txt")
            with open(sample, "w") as f:
                f.write("hello world")
            result = size(tmpdir)
            assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            size("")
        except (ValueError, TypeError, FileNotFoundError, OSError):
            pass  # Expected for path-based utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = size(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
