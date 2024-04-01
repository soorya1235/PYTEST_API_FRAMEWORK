import logging
import os

import pytest

print("Current dir is", os.getcwd())


class TestLogger:
    @pytest.fixture(autouse=True)
    def set_logger(self, initialize_logger):
        self.logger = initialize_logger

    # Define a Pytest test function
    def test_logging_example_1(self):
        # Use the logger to log messages
        self.logger.info("This is an informational message.")
        # Assertion to pass the test
        assert 1 == 1

    def test_logging_example_2(self):
        # Use the logger to log messages
        self.logger.warning("This is a warning message.")
        assert 1 == 1

    def test_logging_example_3(self):
        # Use the logger to log messages
        self.logger.critical("This is a critical message.")
        assert 1 == 1

    def test_logging_example_4(self):
        # Use the logger to log messages
        self.logger.critical("This is a critical message.")
        assert 1 == 1


