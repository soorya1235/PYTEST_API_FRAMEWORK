"""
This module will test the sample request
"""
import requests
import json
from Utilities.configurations import *
from Resources.ApplicationsService import Applications
from Resources.Configuration import AUT


class TestApplication:

    def test_get_request_1(self):
        ip = get_aut_configuations()['API']['endpoint']
        end_point = Applications.testApi.format(ip)
        print(end_point)
        response = requests.get('http://216.10.245.166/Library/GetBook.php',
                                params={'AuthorName': 'Rahul Shetty'}, )
        print(response.status_code)
        # print(response.text)
        # print(type(response.text))
        # dict_response = json.loads(response.text)
        # print(dict_response[0]['isbn'])
        # json_response = response.json()

    # def test_get_request_2(self):
    #     pass
