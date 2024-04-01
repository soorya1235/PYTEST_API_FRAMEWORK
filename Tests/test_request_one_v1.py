"""
This module will test the sample request
"""
import logging

import requests

from Resources.application_service import Applications
from Utilities.configurations import get_aut_configurations


class TestApplication:

    @classmethod
    def setup_class(cls):
        print("Setting up class")
        #cls.timeout = 60

    def test_get_request_1(self):
        url = Applications.test_api.format(get_aut_configurations()['API']['ip'])
        print(url)

        # Below is one way of using the setup_class where define the timeout and use it as self.timeout in below line.
        # response = requests.get(url, params={'AuthorName': 'Rahul Shetty'}, timeout=self.timeout)

        response = requests.get(url, params={'AuthorName': 'Rahul Shetty'}, timeout=self.timeout)
        print(response.status_code)
        logging.info("Response code: %s", str(response.status_code))
        assert response.status_code == 200, "Response Code did not Match"


    def test_get_request_2(self):
        url = Applications.add_book.format(get_aut_configurations()['API']['ip'])
        print(url)
        #response = requests.get(url, params={'AuthorName': 'Rahul Shetty'}, timeout=60)