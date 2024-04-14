"""
Now we have fixture_demo defined in the conftest.py file,
how to use it.

2Ways
1)simply import at each of the test_method as paramter, if we dont import it will not be called.
2)Import it at class level
"""


class Test_fixture_conftest:

    def test_method1(self, fixture_demo):
        print("test1")

    def test_method2(self, fixture_demo):
        print("test2")

    def test_method3(self, fixture_demo):
        print("test2")
