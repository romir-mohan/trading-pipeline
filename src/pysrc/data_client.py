from typing import Any, List, Dict
import requests
import json
import time


class DataClient:
    def __init__(self) -> None:
        self.max_retries = 5
        self.retry_delay = 5

    def _query_api(self) -> List[Dict[str, Any]]:
        url = "https://api.sandbox.gemini.com/v1/trades/btcusd"
        retries = 0

        while retries < self.max_retries:
            try:
                response = requests.get(url)
                response.raise_for_status()
                data: List[Dict[str, Any]] = response.json()
                return data
            except (requests.RequestException, ValueError) as e:
                print(f"Attempt {retries + 1} failed: {e}")
                retries += 1
                if retries < self.max_retries:
                    print(f"Retrying in {self.retry_delay} seconds...")
                    time.sleep(self.retry_delay)
                else:
                    raise ValueError("API request failed after multiple retries")

        raise ValueError("API request failed after multiple retries")

    def _parse_message(
        self, messages: list[dict[str, Any]]
    ) -> list[tuple[list[float], float]]:
        trades = []

        for x in messages:
            if type(x) is dict:
                price = float(x["price"])
                amount = float(x["amount"])

                features = [price, amount]

                midprice = price

                trade = (features, midprice)

                trades.append(trade)

        return trades

    def get_data(self) -> list[tuple[list[float], float]]:
        data = self._query_api()

        return self._parse_message(data)
