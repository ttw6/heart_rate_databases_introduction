import pytest
from server import *


def validate_heart_rate_requests(r):
    data = {
        "user_email": "suyash@suyashkumar.com",
        "user_age": 50,
        "heart_rate": 100
    }

    assert not jsonify(data)


def test_tachy():
    assert is_tachy(15, 200) == "True"
    assert is_tachy(15, 90) == "False"
    assert is_tachy(4, 150) == "True"
