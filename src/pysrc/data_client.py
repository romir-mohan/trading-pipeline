from typing import Any
import requests
import json
import time


class DataClient:
    def __init__(self) -> None:
        self.api_url = "https://api.sandbox.gemini.com/v1/trades/btcusd"

    def _query_api(self) -> list[dict[str, Any]]:
        retries = 3

        for attempt in range(retries):
            try:
                response = requests.get(self.api_url, timeout=5)

                print(f"Attempt {attempt + 1}: Status Code {response.status_code}")

                if response.status_code == 200:
                    if not response.text.strip():
                        raise ValueError("API response is empty")

                    try:
                        data: list[dict[str, Any]] = response.json()
                        return data
                    except json.JSONDecodeError:
                        raise ValueError("Failed to decode JSON from API response")

                print(f"Retrying in 2 seconds... ({attempt + 1}/{retries})")
                time.sleep(2)

            except requests.RequestException as e:
                print(f"Request failed: {e}")

        raise ValueError("API request failed after multiple retries")

    def _parse_message(
        self, messages: list[dict[str, Any]]
    ) -> list[tuple[float, float, bool]]:
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
