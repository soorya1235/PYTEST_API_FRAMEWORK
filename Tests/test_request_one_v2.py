"""
This is extension of test_request_one.py where i have not use the auto use ,
here i defined a fixture at class level and use it at class level, so that
it will be avaiable for all the testcases.
"""

import logging
import pytest
import requests

from Resources.application_service import Applications
from Utilities.configurations import get_aut_configurations


@pytest.mark.usefixtures("timeout_use_class")
class TestApplication:

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
        # response = requests.get(url, params={'AuthorName': 'Rahul Shetty'}, timeout=60)
