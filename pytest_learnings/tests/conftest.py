import pytest


@pytest.fixture(scope="session")
def fixture_example_conftest():
    yield "hello world"
    print("closing fixture")


@pytest.fixture(scope="class")
def class_level_fixture():
    print("I will be executing first")
    yield
    print("I will be executing last")


@pytest.fixture()
def data_load():
    return ["abcd", "bbb", "eee"]


@pytest.fixture(params=["chrome", "firefox", "IE"])
def multiple_data_sets(request):
    return request.param


@pytest.fixture(autouse=True)
def auto_use_fixture():
    print("Auto use fixture called")
