"""Tests for the `cli` module."""

# import pytest

# from demoagent import cli


def test_main():
    """Basic CLI test."""
    assert cli.main([]) == 0


def test_show_help(capsys):
    """
    Show help.

    Arguments:
        capsys: Pytest fixture to capture output.
    """
    pass


#   with pytest.raises(SystemExit):
#      cli.main(["-h"])
# captured = capsys.readouterr()
# assert "demoagent" in captured.out
