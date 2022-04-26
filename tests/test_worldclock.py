import os

import pytest
from freezegun import freeze_time

from pybites_tools import worldclock
from pybites_tools.worldclock import WorldClockException


@freeze_time("2021-10-17 13:30:00")
@pytest.mark.parametrize(
    "args, expected",
    [
        (
            [],
            (
                "Europe/Berlin             03:30PM\n"
                "Australia/Sydney          12:30AM\n"
                "America/Los_Angeles       06:30AM\n"
            ),
        ),
        (
            [22, 55, 2022, 4, 1, "Europe/London"],
            (
                "Europe/Berlin             11:55PM\n"
                "Australia/Sydney          08:55AM\n"
                "America/Los_Angeles       02:55PM\n"
            ),
        ),
        (
            [0, 1, 2022, 4, 1, "UTC"],
            (
                "Europe/Berlin             02:01AM\n"
                "Australia/Sydney          11:01AM\n"
                "America/Los_Angeles       05:01PM\n"
            ),
        ),
        (
            [0, 1, 2022, 3, 1, "UTC"],
            (
                "Europe/Berlin             01:01AM\n"
                "Australia/Sydney          11:01AM\n"
                "America/Los_Angeles       04:01PM\n"
            ),
        ),
    ],
)
def test_worldclock(monkeypatch, capsys, args, expected):
    mock_env = {
        "TIMEZONE_LIST": '["Europe/Berlin", "Australia/Sydney", "America/Los_Angeles"]'
    }
    monkeypatch.setattr(os, "environ", mock_env)
    worldclock.convert_time(*args)
    captured = capsys.readouterr()
    assert captured.out == expected


def test_bad_timezone_json(monkeypatch, capsys):
    mock_env = {"TIMEZONE_LIST": '["CET" "Australia/Sydney", "America/Los_Angeles"]'}
    monkeypatch.setattr(os, "environ", mock_env)
    with pytest.raises(WorldClockException, match="JSON error.*syntax"):
        worldclock.convert_time()


def test_bad_timezone_entered(monkeypatch, capsys):
    mock_env = {"TIMEZONE_LIST": '["CET", "America/Los_Amos"]'}
    monkeypatch.setattr(os, "environ", mock_env)
    with pytest.raises(WorldClockException, match="UnknownTimeZoneError.*correctly"):
        worldclock.convert_time()
