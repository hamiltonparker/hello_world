"""Tests the mathematical functions defined in math.py
"""

import pytest

def test_square:
    """Tests the squaring function"""
    from demo.math import square

    assert 4 == square(2)
