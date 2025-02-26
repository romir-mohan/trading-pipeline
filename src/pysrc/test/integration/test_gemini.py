from pysrc.intern import DataClient
import requests

def test_gemini() -> None:
    client = DataClient()
    trades = client.get_data()

    assert type(trades[0][0]) is float
    assert type(trades[0][1]) is float
    assert type(trades[0][2]) is bool
  
    assert len(trades) > 0
