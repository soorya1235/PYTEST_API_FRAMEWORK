"""
Example of tearn_down class where it will be called after all the test is executed
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
