import pytest


@pytest.mark.usefixtures("auto_use_fixture")
class Testautousefixture:

    def test_one(self):
        print("testing auto use fixture test one")

    def test_two(self):
        print("testing auto use fixture test two")
