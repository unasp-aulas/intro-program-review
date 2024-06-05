import pytest
from problem_5 import main


@pytest.mark.parametrize(
    "dist,expected",
    [
        (201, 90.45),
        (300, 135.0),
        (500, 175.0)
    ],
)
def test_problem_5(dist, expected):
    assert main(dist) == expected
