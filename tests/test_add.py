# =========================
# Test Code (pytest)
# =========================

from app import is_even, Calculator


def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5


def test_subtract():
    calc = Calculator()
    assert calc.subtract(5, 3) == 2


def test_multiply():
    calc = Calculator()
    assert calc.multiply(4, 3) == 12


def test_divide():
    calc = Calculator()
    assert calc.divide(10, 2) == 5


def test_divide_by_zero():
    calc = Calculator()
    try:
        calc.divide(5, 0)
        assert False  # should not reach here
    except ValueError:
        assert True


def test_is_even_true():
    assert is_even(4) is True


def test_is_even_false():
    assert is_even(7) is False

def test_is_even_zero():
    assert is_even(0) is True

def test_is_even_negative():
    assert is_even(-2) is False

def test_is_even_float():
    assert is_even(3.14) is False

def test_is_even_string():
    assert is_even("hello") is False

def test_is_even_list():
    assert is_even([1, 2, 3]) is False

def test_is_even_none():
    assert is_even(None) is False

def test_is_even_dict():
    assert is_even({"a": 1, "b": 2}) is False

def test_is_even_tuple():
    assert is_even((1, 2, 3)) is False

def test_is_even_set():
    assert is_even({1, 2, 3}) is False

def test_is_even_large_number():
    assert is_even(1000000) is True

def test_is_even_negative_large_number():
    assert is_even(-1000000) is True

def test_is_even_non_integer():
    assert is_even(2.5) is False

def test_is_even_boolean():
    assert is_even(True) is False
    assert is_even(False) is True

def test_is_even_empty_string():
    assert is_even("") is False