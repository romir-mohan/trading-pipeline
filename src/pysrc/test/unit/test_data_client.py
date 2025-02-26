from unittest.mock import patch
from typing import Any, List, Dict

from pysrc.data_client import DataClient

trades_map: List[Dict[str, Any]] = [
    {
        "timestamp": 1,
        "timestampms": 1000,
        "tid": 1,
        "price": "101",
        "amount": "30",
        "exchange": "gemini",
        "type": "sell",
    },
    {
        "timestamp": 2,
        "timestampms": 2000,
        "tid": 2,
        "price": "202",
        "amount": "20",
        "exchange": "gemini",
        "type": "buy",
    },
    {
        "timestamp": 3,
        "timestampms": 3000,
        "tid": 3,
        "price": "303.3",
        "amount": "33.3",
        "exchange": "gemini",
        "type": "sell",
    },
  {
        "timestamp": 4,
        "timestampms": 4123,
        "tid": 4,
        "price": "404.4",
        "amount": "44.4",
        "exchange": "gemini",
        "type": "buy",
    },
]

def test__parse_message() -> None:
    client = DataClient()

    with patch.object(client, "_query_api") as mock_query_api:
        mock_query_api.return_value = trades_map

        data = client._query_api()
        trades = client._parse_message(data)

        assert len(trades) == 4
        assert trades[0][0] == 101

def test_get_data() -> None:
    client = DataClient()

    with patch.object(client, "_query_api") as mock_query_api:
        mock_query_api.return_value = trades_map

        trades = client.get_data()

        assert len(trades) == 4
        assert trades[0][0] == 101
