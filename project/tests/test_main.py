"""Unit tests for the app.main module."""

import pytest
from app.main import add, subtract, multiply, divide, floor_division

def test_add():
    """Test for addition of two numbers in app.main module."""
    assert add(3, 5) == 8
    assert add(-1, 1) == 0

def test_subtract():
    """Test for subtraction of two numbers in app.main module."""
    assert subtract(10, 4) == 6
    assert subtract(0, 5) == -5

def test_multiply():
    """Test for multiplication of two numbers in app.main module."""    
    assert multiply(3, 7) == 21
    assert multiply(-1, 5) == -5
    assert multiply(0, 5) == 0
    assert multiply(5, 0) == 0

def test_divide():
    """Test for division of two numbers in app.main module."""
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    with pytest.raises(ValueError):
        divide(5, 0)

def test_floor_division():
    """Test for floor division of two numbers in app.main module."""
    assert floor_division(7, 2) == 3
    assert floor_division(7.0, 2) == 3.0
    assert floor_division(-7, 2) == -4
    assert floor_division(5, 2.0) == 2.0
    with pytest.raises(ValueError):
        floor_division(5, 0)
