"""
To determine the scope of a fixture in pytest, you can inspect the fixture definition itself.
The scope of a fixture is specified when defining the fixture function using the @pytest.fixture decorator.

Here's how you can determine the scope of a fixture:

In this example:

We define a fixture named my_fixture with a scope of "function".
We access the scope attribute of the fixture object using my_fixture._pytestfixturefunction.scope.
We print out the scope of the fixture.
The output will indicate the scope of the fixture, which can be one of the following:

"function": The fixture will be invoked once per test function (default scope).
"class": The fixture will be invoked once per test class.
"module": The fixture will be invoked once per test module.
"package": The fixture will be invoked once per test package.
"session": The fixture will be invoked once per test session.
This approach allows you to inspect the scope of any fixture defined in your pytest test suite.
"""

import pytest


@pytest.fixture(scope="function")
def my_fixture():
    pass


@pytest.fixture(scope="class")
def class_fixture():
    pass


def test_scope():
    scope = my_fixture._pytestfixturefunction.scope
    print("Scope of my_fixture:", scope)
    scope1 = class_fixture._pytestfixturefunction.scope
    print("Scope of class_fixture:", scope1)
