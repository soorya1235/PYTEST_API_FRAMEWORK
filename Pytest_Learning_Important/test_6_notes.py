"""
Pytest does not enforce strict naming conventions for tests, but there are some widely accepted conventions that
help improve readability and maintainability of test suites. Here are some common pytest test naming conventions:

Test Functions: Test functions should start with test_ prefix. This makes it easy for pytest to discover and run
the tests. For example:

def test_addition():
    assert 1 + 2 == 3

Test Classes: Test classes should typically start with Test prefix, followed by a descriptive name. Inside the class,
test methods should start with test_. This makes it clear that the class contains test cases. For example:

class TestMathFunctions:
    def test_addition(self):
        assert 1 + 2 == 3

Pytest expects our tests to be located in files whose names begin with test_ or end with _test.py.

"""