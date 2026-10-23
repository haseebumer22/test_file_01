
from Working import Working


def test_addition():
    result = Working(10, 5)
    assert result[0] == 15


def test_subtraction():
    result = Working(10, 5)
    assert result[1] == 5


def test_multiplication():
    result = Working(10, 5)
    assert result[2] == 50


def test_zero_edge_case():
    result = Working(0, 5)
    assert result == (5, -5, 0)


def test_negative_numbers():
    result = Working(-10, -5)
    assert result == (-15, -5, 50)
