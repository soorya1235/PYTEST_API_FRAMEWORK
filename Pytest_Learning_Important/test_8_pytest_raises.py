# test_capitalize.py

import pytest


"""
In the below example when we exeucte the testcase test case will fail with error
AttributeError: 'int' object has no attribute 'capitalize',because we are passing
integer, so in order to over this error we can use pytest.raises wher we expect
AttributeError and if place "AttributeError" instead of "TypeError".
Testcase will Pass.

1.Run without out commenting "test_raises_exception_on_non_string_arguments"
you will see the error
2.Run commenting the above testcase, 3 rd testcase will pass, even though 
Attribute error is thrown.


"""


def capital_case(x):
    return x.capitalize()


def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'


def test_raises_exception_on_non_string_arguments():
    with pytest.raises(TypeError):
        capital_case(9)


def test_raises_exception_on_non_string_arguments_1():
    with pytest.raises(AttributeError):
        capital_case(9)

