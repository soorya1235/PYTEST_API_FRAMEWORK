import pytest


@pytest.mark.usefixtures("data_load")
class TestDataDrivenFixture:

    def test_one(self, data_load):
        print(data_load[0])
        print(data_load[1])
        print(data_load[2])
