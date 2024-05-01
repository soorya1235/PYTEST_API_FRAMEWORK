import pytest
from datetime import datetime


# Define your fixture


# Use the fixture in a test class
class TestSomething:
    date = None  # Class attribute to hold the date

    def get_date(self):
        # Return the current date
        return datetime.now().date()

    @classmethod
    def setup_class(cls):
        # Get the current date using the fixture
        instance = cls()
        # Get the current date using the method
        cls.date = instance.get_date()
        print(cls.date)

    def test_date(self):
        # Use the date in your test
        assert self.date == datetime.now().date()

    # def test_date1(self):
    #     # Use the date in your test
    #     assert self.date == datetime.now().date()
