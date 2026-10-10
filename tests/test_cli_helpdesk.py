import subprocess
import sys


def test_cli_it_helpdesk():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "assistant",
            "where is the IT helpdesk?",
        ],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert "IT Helpdesk" in result.stdout