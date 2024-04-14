"""
Now we have fixture_demo defined in the conftest.py file,
how to use it.

2Ways
1)simply import at each of the test_method as paramter, if we dont import it will not be called.
2)Import it at class level, there is no need to import it at each test method.

IF you see the output of below, since fxiture_demo defautl scope is function, it is called before
each and after function.
"""

import pytest


@pytest.mark.usefixtures("fixture_demo")
class Test_fixture_conftest:

    def test_method1(self):
        print("test1")

    def test_method2(self):
        print("test2")

    def test_method3(self):
        print("test2")
