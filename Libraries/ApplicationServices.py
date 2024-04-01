""""
This Module will contain the APIs related to Application Services
"""
import logging

import requests

from Resources.application_service import Applications
from Utilities.configurations import get_aut_configurations
import pytest


class ApplicationService:
    # logger = None

    # @pytest.fixture(autouse=True, scope='class')
    # def set_logger(self, get_class_logger):
    #     ApplicationService.logger = get_class_logger

    # def __init__(self, logger):
    #     self.logger = logger

    _logger = None

    @classmethod
    def set_logger(cls, logger):
        cls._logger = logger

    @classmethod
    def logger(cls):
        return cls._logger

    @staticmethod
    def get_books():
        """
        Returns:
        response_data (dict) : List of books
        """
        logger = ApplicationService.logger()
        response_data = {}
        url = Applications.test_api.format(get_aut_configurations()['API']['ip'])
        # Below is one way of using the setup_class where define the timeout and use it as self.timeout in below line.
        # response = requests.get(url, params={'AuthorName': 'Rahul Shetty'}, timeout=self.timeout)

        logger.debug("Execution of add_book => %s", url)
        logger.debug("Timeout Value is => %s", get_aut_configurations()['Timeout'])
        try:
            response = requests.get(url, params={'AuthorName': 'Rahul Shetty'},
                                    timeout=int(get_aut_configurations()['Timeout']['value']))
        except requests.exceptions.RequestException as e:
            logger.error("Request failed: %s", e)
            response_data['error'] = str(e)
            return response_data
        logger.debug("Execution of add_book completed")
        logger.debug("Response code: %s", str(response.status_code))
        response_data['status_code'] = response.status_code
        response_data['data'] = response.json()
        return response_data
