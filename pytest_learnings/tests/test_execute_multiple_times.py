import pytest


class Testmultipletimes:

    @pytest.mark.parametrize("scene, scenario2", [("one", "two"), ("three", "four")])
    def test_multiple_scenarios(self, scene, scenario2):
        print(f"Scenario 1: {scene}, Scenario 2: {scenario2}")
        assert 1 == 1

    test_cases = [
        ("test_case_1", ["one", "two", "three"]),
        ("test_case_2", ["four", "five", "six"])
    ]

    @pytest.mark.parametrize("testcase, parameters", test_cases)
    def test_multiple_scenarios(self, testcase, parameters):
        print(f"Test case: {testcase}")
        for param in parameters:
            print(f"Parameter: {param}")

    def test_test_three(self):
        assert 3 == 3
