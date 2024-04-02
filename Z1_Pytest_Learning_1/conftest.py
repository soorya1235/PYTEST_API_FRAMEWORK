# conftest.py

import pytest
import sys
import os
import logging


@pytest.fixture()
def learning_function_scope_fixture():
    print("--In Function Scope Enter---")
    yield
    print("--Out of Function Scope---")


@pytest.fixture(scope="class")
def learning_class_scope_fixture():
    print("--In class Scope Enter---")
    yield
    print("--Out of class Scope---")
