from pysrc.data_client import DataClient


def test_data() -> None:
    data_client = DataClient()
    data = data_client.get_data()

    assert isinstance(first_trade, tuple)
