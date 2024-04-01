"""
Setup Method will be called before each testcase,here is the code to prove that.
"""


class TestExample:
    def setup_method(self):
        print("Setting up")

    def test_one(self):
        print("Test one")

    def test_two(self):
        print("Test two")
