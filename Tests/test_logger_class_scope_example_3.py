# test_logger_class_scope_example_3.py
import pytest


class TestLogger:
    @pytest.fixture(autouse=True, scope='class')
    def set_logger(self, get_class_logger):
        self.logger = get_class_logger

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
