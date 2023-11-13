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
            [None, None, None, None, None, None, True],
            (
                "Europe/Berlin             03:30PM   17 Oct 2021\n"
                "Australia/Sydney          12:30AM   18 Oct 2021\n"
                "America/Los_Angeles       06:30AM   17 Oct 2021\n"
            ),
        ),
        (
            [22, 55, 2022, 4, 1, "Europe/London", True],
            (
                "Europe/Berlin             11:55PM   01 Apr 2022\n"
                "Australia/Sydney          08:55AM   02 Apr 2022\n"
                "America/Los_Angeles       02:55PM   01 Apr 2022\n"
            ),
        ),
        (
            [0, 1, 2022, 4, 1, "UTC", True],
            (
                "Europe/Berlin             02:01AM   01 Apr 2022\n"
                "Australia/Sydney          11:01AM   01 Apr 2022\n"
                "America/Los_Angeles       05:01PM   31 Mar 2022\n"
            ),
        ),
        (
            [0, 1, 2022, 3, 1, "UTC", True],
            (
                "Europe/Berlin             01:01AM   01 Mar 2022\n"
                "Australia/Sydney          11:01AM   01 Mar 2022\n"
                "America/Los_Angeles       04:01PM   28 Feb 2022\n"
            ),
        ),
        (
            [20, 50, 2022, 12, 31, "UTC", True],
            (
                "Europe/Berlin             09:50PM   31 Dec 2022\n"
                "Australia/Sydney          07:50AM   01 Jan 2023\n"
                "America/Los_Angeles       12:50PM   31 Dec 2022\n"
            ),
        ),
    ],
)
def test_worldclock_with_date_offset(monkeypatch, capsys, args, expected):
    mock_env = {
        "TIMEZONE_LIST": '["Europe/Berlin", "Australia/Sydney", "America/Los_Angeles"]'
    }
    monkeypatch.setattr(os, "environ", mock_env)
    worldclock.convert_time(*args)
    captured = capsys.readouterr()
    assert captured.out == expected
