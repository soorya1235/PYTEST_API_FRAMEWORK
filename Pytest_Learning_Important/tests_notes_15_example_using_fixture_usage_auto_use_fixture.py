"""

Now i have added auto fixture in the conftest.py file, this will be called
automatically, by default its scope is function level and it will called at each
function. now exeucte this file, if you see the output you will see that it will
be called at each function level.
"""

import pytest


@pytest.mark.usefixtures("class_scope_demo")
class Test_fixture_conftest:

    def test_method1(self):
        print("test1")

    def test_method2(self):
        print("test2")

    def test_method3(self):
        print("test2")
