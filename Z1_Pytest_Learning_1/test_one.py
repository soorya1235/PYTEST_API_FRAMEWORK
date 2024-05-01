import pytest
from datetime import datetime


def get_date(self):
    # Return the current date
    return datetime.now().date()


# Use the fixture in a test class
class TestSomething:
    date = None  # Class attribute to hold the date

    @classmethod
    def setup_class(cls):
        # Get the current date using the fixture
        cls.date = get_date()

    def test_date(self):
        # Use the date in your test
        assert self.date == datetime.now().date()

    # def test_date1(self):
    #     # Use the date in your test
    #     assert self.date == datetime.now().date()
