import pytest

"""
defaut scope of this fixture is function,
it will called for each function.
"""


@pytest.fixture()
def fixture_demo():
    print("This is fixture demo called from conftest file")
    yield
    print("This is fixture demo ended from conftest file")


@pytest.fixture(scope="class")
def class_scope_demo():
    print("This is class scope fixture demo called from conftest file")
    yield
    print("This is class scope fixture demo ended from conftest file")


@pytest.fixture(autouse=True)
def auto_use_fixture():
    print("This is auto use fixture called from conftest file")
    yield
    print("This is auto use fixture called from conftest file")


@pytest.fixture(autouse=True, scope="class")
def auto_use_fixture_class_level():
    print("This is auto use fixture called from conftest file")
    yield
    print("This is auto use fixture called from conftest file")
