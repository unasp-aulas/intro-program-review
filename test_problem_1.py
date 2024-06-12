import pytest
from problem_1 import main


@pytest.mark.parametrize(
    "cargo,salario,expected",
    [
        ("junior", 1000, 1150.0),
        ("pleno", 1000, 1260.0),
        ("senior", 1000, 1340.0),
        ("outro", 1000, -1),
    ],
)
def test_problem_1(cargo, salario, expected):
    assert main(cargo, salario) == expected
