import builtins
import importlib
import io
import sys
from pytest import MonkeyPatch


def test_problem_3(monkeypatch: MonkeyPatch):
    def mocked_input(prompt="", return_vals=["0", "3", "6", "4"]):
        return return_vals.pop(-1)

    mocked_stdout = io.StringIO()

    with monkeypatch.context() as m:
        m.setattr(builtins, "input", mocked_input)
        m.setattr(sys, "stdout", mocked_stdout)

        sys.modules.pop("problem_3", None)
        importlib.import_module(name="problem_3", package="")

    assert mocked_stdout.getvalue().strip() == "13"
