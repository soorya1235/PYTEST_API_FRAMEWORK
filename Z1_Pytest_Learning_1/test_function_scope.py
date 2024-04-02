"""
Below is an example of function scope fixture.
I have created a fixture in the conftest by name learning_function_scope_fixture.
"""


def test_function_1(learning_function_scope_fixture):
    print("Function 1")


def test_function_2(learning_function_scope_fixture):
    print("Function 2")


def test_function_3(learning_function_scope_fixture):
    print("Function 3")
