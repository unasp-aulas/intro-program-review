import builtins
import importlib
import io
import sys
from pytest import MonkeyPatch


def test_problem_4(monkeypatch: MonkeyPatch):
    def mocked_input(prompt=""):
        return {"Qual o valor da casa? ": 100000, "Qual é o salário? ": 10000, "Pagar em quantos anos? ": 10}[prompt]

    mocked_stdout = io.StringIO()

    with monkeypatch.context() as m:
        m.setattr(builtins, "input", mocked_input)
        m.setattr(sys, "stdout", mocked_stdout)

        sys.modules.pop("problem_4", None)
        importlib.import_module(name="problem_4", package="")

    assert mocked_stdout.getvalue().strip() == "Aprovado"
