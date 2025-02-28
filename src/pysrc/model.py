from typing import Any, Optional
from sklearn.linear_model import Lasso


class Model:
    def __init__(self) -> None:
        self._train_length = 10
        self._features: list[list[float]] = []
        self._midprices: list[float] = []
        self._targets: list[float] = []
        self._model = Lasso()
        self._time = 0
        self._previous: Optional[float] = None

        self._filepath = "src/pysrc/data/test_data.txt"
        with open(self._filepath, "w") as _:
            pass

    def _find_target(self, midprice: float) -> None:
        if len(self._midprices) > 0:
            self._targets.append(midprice - self._midprices[-1])

            if len(self._targets) > self._train_length:
                self._targets = self._targets[1:]

    def _add_data(self, features: list[float], midprice: float) -> None:
        self._midprices.append(midprice)
        self._features.append(features)

        if len(self._features) > self._train_length:
            self._features = self._features[1:]
            self._midprices = self._midprices[1:]

    def predict(self, data: tuple[list[float], float]) -> Optional[float]:
        features = data[0]
        midprice = data[1]

        self._find_target(midprice)

        print(f"Current features length: {len(self._features)}")

        if len(self._features) == self._train_length:
            if self._previous is not None:
                with open(self._filepath, "a") as file:
                    file.write(
                        f"Time: {self._time}\n"
                        f"Expected: {self._previous}\n"
                        f"Actual: {self._targets[-1]}\n"
                    )
                    print(f"Data written at time {self._time}")

            self._model.fit(self._features, self._targets)
            prediction: float = self._model.predict([features])[0]

            self._time += 1
            self._previous = prediction
            self._add_data(features, midprice)

            return prediction

        else:
            self._add_data(features, midprice)
            return None
