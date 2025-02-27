from pysrc.model import Model
from pytest import approx


def test__find__target() -> None:
    model = Model()
    model._find_target(10.1)
    assert len(model._targets) == 0

    model._midprices.append(12.0)

    model._find_target(12.5)
    assert len(model._targets) == 1
    assert model._targets[0] == 0.5


def test__add_data() -> None:
    model = Model()

    for i in range(10):
        model._add_data([i, i + 1, i + 2, i + 3], float(i))
        assert len(model._features) == i + 1
        assert len(model._midprices) == i + 1
        assert model._features[i] == [i, i + 1, i + 2, i + 3]
        assert model._midprices[i] == approx(float(i))

    model._add_data([10, 11, 12, 13], 10.0)
    assert len(model._features) == 10
    assert len(model._midprices) == 10
    assert model._features[0] == [1, 2, 3, 4]
    assert model._midprices[0] == approx(1.0)
    assert model._features[-1] == [10, 11, 12, 13]
    assert model._midprices[-1] == approx(10.0)

    model._add_data([11, 12, 13, 14], 11.0)
    assert len(model._features) == 10
    assert len(model._midprices) == 10
    assert model._features[0] == [2, 3, 4, 5]
    assert model._midprices[0] == approx(2.0)
    assert model._features[-1] == [11, 12, 13, 14]
    assert model._midprices[-1] == approx(11.0)


def test_predict() -> None:
    model = Model()

    for i in range(10):
        assert model.predict(([i, i + 1, i + 2, i + 3], float(i))) is None

    assert model.predict(([11, 12, 13, 14], 10.0)) is not None
    assert model.predict(([12, 13, 14, 15], 11.0)) is not None
    assert model.predict(([13, 14, 15, 16], 12.0)) is not None
    assert model.predict(([14, 15, 16, 17], 13.0)) is not None
    assert model.predict(([15, 16, 17, 18], 14.0)) is not None
    assert model.predict(([16, 17, 18, 19], 15.0)) is not None

    for i in range(20, 30):
        assert model.predict(([i, i + 1, i + 2, i + 3], float(i))) is not None

    assert model.predict(([30, 31, 32, 33], 30.0)) is not None
    assert model.predict(([31, 32, 33, 34], 31.0)) is not None
    assert model.predict(([32, 33, 34, 35], 32.0)) is not None
