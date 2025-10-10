# test_math_utils.py
# Unit tests for math_utils.py using pytest

import pytest
from math_utils import add, subtract, multiply, divide, average

def test_add():
    """
    Test the add function with various inputs.
    @param: na
    @:return: na
    @ exceptions: na
    """
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    """
    Test the add function with various inputs.
    @param: na
    @:return: na
    @ exceptions: na
    """
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5
    assert subtract(-2, -2) == 0

def test_multiply():
    """
    Test the add function with various inputs.
    @param: na
    @:return: na
    @ exceptions: na
    """
    assert multiply(3, 4) == 12
    assert multiply(0, 10) == 0
    assert multiply(-2, 3) == -6

def test_divide():
    """
    Test the add function with various inputs.
    @param: na
    @:return: na
    @ exceptions: ValueError for division by zero
    """
    assert divide(10, 2) == 5
    assert divide(-9, 3) == -3
    with pytest.raises(ValueError):
        divide(5, 0)

def test_average():
    """
    Test the add function with various inputs.
    @param: na
    @:return: na
    @ exceptions: ValueError for empty list
    """
    assert average([2, 4, 6, 8]) == 5
    assert pytest.approx(average([1, 2, 3])) == 2.0
    with pytest.raises(ValueError):
        average([])
