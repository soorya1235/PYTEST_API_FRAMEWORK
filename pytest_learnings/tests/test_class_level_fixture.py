import pytest


@pytest.mark.usefixtures("class_level_fixture")
class TestClassLevelFixture:

    def test_one(self):
        print("test one")

    def test_two(self):
        print("test two")