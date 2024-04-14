"""

Since the autouse fixture is called a function level,i need to make it called
at class level or session or package level, how to do it.
add the scope paramter to the autouse fixture.

Now i have added "class_scope_demo" auto use fixture defined at class level,
we will run the below script now.
you will see that class scope auto use fixture will be called once at begining
and end, by default there is function level fixture , that will be called
at each of the function.

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
