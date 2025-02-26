from typing import Any
from requests import get
from json import json

class DataClient:
    def __init__(self) -> None:
        pass

    def _query_api(self) -> list[dict[str, Any]]:
        
        url = "https://api.sandbox.gemini.com/v1/trades/btcusd"

        response = get(url)
        data: list[dict[str, Any]] = list(response.json())

        return data

    def _parse_message(self, messages: list[dict[str, Any]]) -> list[tuple[float, float, bool]]:
        
        trades = []

        for x in messages:
            if type(x) is dict:
                price = float(x["price"])
                amount = float(x["amount"])

                if x["type"] == "buy":
                    side = True
                else:
                    side = False

                trade = (price, amount, side)

                trades.append(trade)

        return trades

    def get_data(self) -> list[tuple[float, float, bool]]:
        data = self._query_api()

        return self._parse_message(data)
