import pytest


@pytest.mark.usefixtures("multiple_data_sets")
class Testmultipledatasets:

    def test_multiple_data_sets(self, multiple_data_sets):
        print(multiple_data_sets)
