import pytest


class Testparameterexample:

    @pytest.mark.parametrize("a", "scope")
    def test_parameter_example(self, a):
        print("The value of the parameter is", a)

    @pytest.mark.parametrize("a", ["testing"])
    def test_parameter_example_one(self, a):
        print("The value of the parameter is", a)
