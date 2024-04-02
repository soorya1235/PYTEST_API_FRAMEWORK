import pytest


@pytest.mark.usefixtures("learning_class_scope_fixture", "learning_function_scope_fixture")
class Testclass:

    def test_function_1(self):
        print("Function 1")

    def test_function_2(self):
        print("Function 2")

    def test_function_3(self):
        print("Function 3")
