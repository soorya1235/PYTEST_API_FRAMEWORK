"""
Yes, pytest provides a special method called teardown_method that you can use in your test classes. This method is called
after each test method is executed.
The teardown_method is typically used to clean up any state or resources that were set up for the test.
This might include closing files, disconnecting from databases, deleting test data, etc.
"""


class TestExample:
    def setup_method(self):
        print("Setting up")

    def teardown_method(self):
        print("Tearing down")

    def test_one(self):
        print("Test one")

    def test_two(self):
        print("Test two")
