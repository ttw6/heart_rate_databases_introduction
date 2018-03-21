import pytest
import client


def validate_heart_rate_requests(r):
    data = {
        "user_email": "suyash@suyashkumar.com",
        "user_age": 50, // in years
        "heart_rate": 100
    }
