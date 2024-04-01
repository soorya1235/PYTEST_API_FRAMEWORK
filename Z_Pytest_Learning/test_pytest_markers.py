# smoke_test.py
import pytest

pytestmark = [pytest.mark.smoke, pytest.mark.fe]


class TestUserSmoke(object):
    def test_user_login(self):
        print("log in")

    def test_user_register(self):
        print("register")
