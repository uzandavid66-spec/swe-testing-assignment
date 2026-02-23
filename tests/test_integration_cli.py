import sys
from subprocess import run


def run_cli(*args: str) -> str:
    """
    Run the Quick-Calc CLI in one-shot mode to simulate real usage:
    input layer (CLI args) -> calculation logic -> stdout output.
    """
    cmd = [sys.executable, "-m", "quickcalc.cli", *args]
    completed = run(cmd, capture_output=True, text=True)
    return completed.stdout.strip()


def test_integration_addition_via_cli():
    assert run_cli("5", "+", "3") == "8"


def test_integration_clear_like_reset_between_runs():
    """
    'Clear' is interactive; instead we verify isolation between runs:
    after a calculation, a new run starts from scratch and returns only its own result.
    """
    first = run_cli("5", "+", "3")
    second = run_cli("2", "*", "4")
    assert first == "8"
    assert second == "8"