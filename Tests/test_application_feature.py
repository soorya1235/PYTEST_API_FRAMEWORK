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

    @pytest.fixture(autouse=True, scope='session')
    def set_logger(self, get_session_logger):
        self.logger = get_session_logger

    def test_get_request_1(self):
        self.logger.info("Starting the Test")
        ApplicationService.set_logger(self.logger)
        response = ApplicationService.get_books()
        self.logger.info("Response Json => %s", response)
        self.logger.info("Ending the Test")
