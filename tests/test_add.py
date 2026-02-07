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