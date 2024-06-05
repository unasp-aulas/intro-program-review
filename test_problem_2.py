import pytest
from problem_2 import main


@pytest.mark.parametrize(
    "ultimo,expected",
    [
        (10, 55),
        (20, 210),
    ],
)
def test_problem_2(ultimo, expected):
    assert main(ultimo) == expected
