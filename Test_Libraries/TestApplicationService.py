import unittest
from unittest.mock import patch, Mock
from Libraries.ApplicationServices import ApplicationService


class TestApplicationService(unittest.TestCase):

    @patch('ApplicationServices.ApplicationService.get_books')
    def test_get_books(self, mock_get):
        # Arrange
        breakpoint()
        mock_response = Mock()
        expected_status_code = 200
        expected_json = {'data': 'test data'}
        mock_response.status_code = expected_status_code
        mock_response.json.return_value = expected_json
        mock_get.return_value = mock_response

        # Act
        result = ApplicationService.get_books()

        # Assert
        self.assertEqual(result['status_code'], expected_status_code)
        self.assertEqual(result['data'], expected_json)
        mock_get.assert_called_once()


if __name__ == '__main__':
    unittest.main()
