from pysrc.data_client import DataClient


def test_data() -> None:
    data_client = DataClient()
    data = data_client.get_data()

    first_trade = data[0]

    assert isinstance(first_trade, tuple)
