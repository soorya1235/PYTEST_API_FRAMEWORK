"""
This Module will contain API related to Application Service and Device Service.
"""


class Applications:
    """
    This Class is having all the API related to Application Service.
    """
    add_book = 'https://{}/Library/Addbook.php'
    delete_book = 'https://{}/Library/DeleteBook.php'
    test_api = 'http://{}/Library/GetBook.php'


class Device:
    """
    This Class is having all the APIS related to Device Service.
    """
    add_device = 'https://{}/Device/AddDevice.php'
