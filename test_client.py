import pytest
from server import *


def validate_input1(r):
    if not isinstance(r["user_email"], str) or \
        not isinstance(r["user_age"], int) or \
        not isinstance(r["heart_rate"], int):
        return "Error in inputs"
    else:
        return "Inputs good"


def validate_input2(r):
    if not isinstance(r["user_email"], str):
        return "Check email"
    else:
        pass
    try:
        datetime.datetime.strptime(r["heart_rate_average_since"], "%Y-%m-%d %H:%M:%S.%f")
    except ValueError:
        raise ValueError("Check date format")
    return "Inputs good"


def test_input1():
    # Working Input
    r1 = {
        "user_email": "suyash@suyashkumar.com",
        "user_age": 50,
        "heart_rate": 100
    }
    # Broken Input
    r2 = {
        "user_email": "suyash@suyashkumar.com",
        "user_age": "no",
        "heart_rate": 100
    }
    assert validate_input1(r1) == "Inputs good"
    assert validate_input1(r2) == "Error in inputs"


def test_input2():
    # Good input
    r1 = {
        "user_email": "suyash@suyashkumar.com",
        "heart_rate_average_since": "2018-03-09 11:00:36.372339"
    }
    # Bad input
    r2 = {
        "user_email": 10,
        "heart_rate_average_since": "2018-03-09 11:00:36.372339"
    }
    # Bad input
    r3 = {
        "user_email": "suyash@suyashkumar.com",
        "heart_rate_average_since": "03-2018-09 11:00:36.372339"
    }
    assert validate_input2(r1) == "Inputs good"
    assert validate_input2(r2) == "Check email"
    with pytest.raises(ValueError):
        validate_input2(r3)


def test_tachy():
    assert is_tachy(15, 200) == "True"
    assert is_tachy(15, 90) == "False"
    assert is_tachy(4, 150) == "True"
