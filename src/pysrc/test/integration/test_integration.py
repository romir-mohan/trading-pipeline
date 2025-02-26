from pysrc.intern import DataClient  # type: ignore


def test_tick() -> None:
    data_client = DataClient()
    data = data_client.tick()
