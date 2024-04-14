"""
Example of setup_class and teardown_class method which will be called before any test exectuion
in the class and after last test exeuction.
"""


class TestApplication:
    @classmethod
    def setup_class(cls):
        print("Setting up class")

    @classmethod
    def teardown_class(cls):
        print("Tearing down class")

    def test_get_request_1(self):
        print("request 1")

    def test_get_request_2(self):
        print("request 2")
