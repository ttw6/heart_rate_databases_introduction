import pytest
import server


def validate_heart_rate_requests(r):
    data = {
        "user_email": "suyash@suyashkumar.com",
        "user_age": 50,
        "heart_rate": 100
    }

    assert not jsonify(data)