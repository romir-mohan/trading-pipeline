from pysrc.data_client import DataClient


def test_tick() -> None:
    data_client = DataClient()
    data = data_client.tick()
