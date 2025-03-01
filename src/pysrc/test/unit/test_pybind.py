import pytest
import intern


def test_pybind() -> None:
    assert intern.add(4, 5) == 9
