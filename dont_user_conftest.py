# dont_user_conftest.py

import pytest
import sys
import os
import logging

"""
Function level fixture which is called for each of testcase.
For this testcase refer test_logger_function_scope_example_3.py
"""


@pytest.fixture(autouse=True)
def get_logger(request):
    # Create a new logger with the test case name as the logger name
    # logger = logging.getLogger(request.node.nodeid)
    test_case_name = request.node.nodeid.split('/')[-1]
    logger = logging.getLogger(test_case_name)
    # Set the log level
    logger.setLevel(logging.DEBUG)
    # Create a file handler
    handler = logging.FileHandler('../Log/test.log')
    # Create a logging format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    # Add the handlers to the logger
    logger.addHandler(handler)
    # Make this logger available to the test case
    request.cls.logger = logger


"""
Module Level Scope Fixture
test_logger_module_scope_example_1.py is used
"""


@pytest.fixture(scope="module")
def get_module_logger(request):
    # Get the test case name without the directory path
    test_case_name = request.node.nodeid.split('/')[-1]
    # Create a new logger with the test case name as the logger name
    logger = logging.getLogger(test_case_name)
    # Set the log level
    logger.setLevel(logging.DEBUG)
    # Create a file handler
    handler = logging.FileHandler('../Log/test.log')
    # Create a logging format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    # Add the handlers to the logger
    logger.addHandler(handler)
    # Return the logger
    return logger


"""
Class level scope fixture
"""


@pytest.fixture(scope='class')
def get_class_logger(request):
    # Get the test case name without the directory path
    test_case_name = request.node.nodeid.split('/')[-1]
    # Create a new logger with the test case name as the logger name
    logger = logging.getLogger(test_case_name)
    # Set the log level
    logger.setLevel(logging.DEBUG)
    # Create a file handler
    handler = logging.FileHandler('../Log/test.log')
    # Create a logging format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    # Add the handlers to the logger
    logger.addHandler(handler)
    # Return the logger
    return logger


@pytest.fixture(scope='session', autouse=True)
def add_utilities_to_sys_path():
    # qGet the absolute path to the parent directory of the current file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    util_dir = os.path.join(current_dir, 'Utilities')
    util_dir = os.path.join(current_dir, 'Resources')  # Adjust this path as needed
    # Append the Utilities folder path to sys.path
    sys.path.append(util_dir)
    print(sys.path)


"""
Yes, you can define a fixture at the class level using pytest's autouse parameter. This will automatically
use the fixture for all test methods in the class. Here's how you can do it:
"""


@pytest.fixture(scope="class", autouse=True)
def setup_timeout(request):
    request.cls.timeout = 60


@pytest.fixture(scope="class")
def timeout_use_class(request):
    request.cls.timeout = 60


@pytest.fixture()
def learning_function_scope_fixture():
    print("--In Function Scope Enter---")
    yield
    print("--Out of Function Scope---")
