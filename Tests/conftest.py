# conftest.py

import pytest
import sys
import os


@pytest.fixture(scope='session', autouse=True)
def add_utilities_to_sys_path():
    #qGet the absolute path to the parent directory of the current file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    util_dir = os.path.join(current_dir, 'Utilities')
    util_dir = os.path.join(current_dir, 'Resources') # Adjust this path as needed
    # Append the Utilities folder path to sys.path
    sys.path.append(util_dir)
    print(sys.path)
