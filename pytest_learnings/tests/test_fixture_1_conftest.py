class TestDemo:

    def test_one_conf_test(self, fixture_example_conftest):
        print("calling from test one conf_test" + fixture_example_conftest)

    def test_two_conf_test(self, fixture_example_conftest):
        print("calling from test one conf_test" + fixture_example_conftest)
