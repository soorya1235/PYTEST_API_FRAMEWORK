import pytest


class TestHowtouseFixture:

    @pytest.fixture
    def return_random_string(self):
        return "hello_works"

    def test_one(self, return_random_string):
        print("called test one" + return_random_string)

    def test_two(self, return_random_string):
        print("called test two" + return_random_string)
