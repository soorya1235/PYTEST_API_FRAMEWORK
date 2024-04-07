"""
This module will test the sample request
"""
import logging

import requests
import pytest

from Resources.application_service import Applications
from Utilities.configurations import get_aut_configurations
from Libraries.ApplicationServices import ApplicationService


class TestApplication:

    # @pytest.fixture(autouse=False, scope='class')
    # def set_logger(self, get_session_logger_v1):
    #     self.logger = get_session_logger_v1

    @pytest.fixture(autouse=True,scope='class')
    def set_logger(self, get_session_logger):
        print("This is called before before class before executing testcases")
        self.logger = get_session_logger
        print("This is called after class fixture executing all testcases")

    def test_get_request_1(self):
        self.logger.info("Starting the Test")
        ApplicationService.set_logger(self.logger)
        response = ApplicationService.get_books()
        self.logger.info("Response Json => %s", response)
        self.logger.info("Ending the Test")

    # def test_get_request_2(self):
    #     print(self.logger)
    #     self.logger.info("Starting the Test2")
    #     self.logger.info("Ending the Test2")

