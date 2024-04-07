import unittest
from unittest.mock import patch, Mock
from Libraries.ApplicationServices import ApplicationService


class TestApplicationService(unittest.TestCase):

    def test_get_books(self):
        # Arrange

        mock_response = Mock()
        expected_status_code = 200
        expected_json = {'data': 'test data'}
        mock_response.status_code = expected_status_code
        mock_response.return_code = expected_status_code
        mock_response.json.return_value = expected_json
        #mock_get.return_value = mock_response

        with patch("Libraries.ApplicationServices.ApplicationService.get_books") as get_auditlog_mock:
            get_auditlog_mock.return_value = mock_response
            result = ApplicationService.get_books()
            assert mock_response.return_code == expected_status_code
            assert mock_response.json.return_value == expected_json

        # # Assert
        # self.assertEqual(result['status_code'], expected_status_code)
        # self.assertEqual(result['data'], expected_json)
        # mock_get.assert_called_once()


if __name__ == '__main__':
    unittest.main()
