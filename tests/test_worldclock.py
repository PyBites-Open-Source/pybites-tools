import os

import pytest
from freezegun import freeze_time

from pybites_tools import worldclock


@freeze_time("2021-10-17 13:30:00")
@pytest.mark.parametrize(
    "args, expected",
    [
        (
            [],
            (
                "CET                       03:30PM\n"
                "Australia/Sydney          12:30AM\n"
                "America/Los_Angeles       06:30AM\n"
            ),
        ),
        (
            [22, 55, "Europe/London"],
            (
                "CET                       11:55PM\n"
                "Australia/Sydney          08:55AM\n"
                "America/Los_Angeles       02:55PM\n"
            ),
        ),
    ],
)
def test_worldclock(monkeypatch, capsys, args, expected):
    mock_env = {"TIMEZONE_LIST": '["CET", "Australia/Sydney", "America/Los_Angeles"]'}
    monkeypatch.setattr(os, "environ", mock_env)
    worldclock.convert_time(*args)
    captured = capsys.readouterr()
    assert captured.out == expected
