"""
Yes, pytest provides a special method called setup_class that is called once for a class
before any test methods or setup methods are called.

The setup_method is a special method in pytest that is automatically called before each test method is executed.
It's typically used to set up any state or resources that are needed for the tests
"""


class TestExample:
    @classmethod
    def setup_class(cls):
        print("Setting up CLASS")

    def setup_method(self):
        print("Setting up METHOD")

    def test_one(self):
        print("Test one")

    def test_two(self):
        print("Test two")
