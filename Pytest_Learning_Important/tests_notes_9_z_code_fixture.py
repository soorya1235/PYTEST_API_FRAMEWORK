import pytest

"""
Here we are declaring a fixture inside the class and if we want to use this fixture
we need to pass them as an argument to the function.
Output file name : tests_notes_9_z_d_output.png

After than execute the file "pytest test_notes_9_z_code_fixture.py --setup-plan
it will show what is the order or execution of fixtures.
"""


class Testfixture:

    @pytest.fixture()
    def my_fixture(self):
        print("I am fixture calling")
        yield
        print("I am fixture ending")

    def test_one(self, my_fixture):
        print("Test One")

    def test_two(self, my_fixture):
        print("Test Two")
