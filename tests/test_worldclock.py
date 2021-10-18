import datetime
import json
import os

import pytest
from freezegun import freeze_time

from pybites_tools import worldclock


@freeze_time("2021-10-17 13:30:00")
def test_now():
    assert datetime.datetime.utcnow() == datetime.datetime(2021, 10, 17, 13, 30, 00)


@freeze_time("2021-10-17 13:30:00")
def test_worldclock(monkeypatch, capsys):
    mock_env = {"TIMEZONE_LIST": '["CET", "Australia/Sydney", "America/Los_Angeles"]'}
    monkeypatch.setattr(os, "environ", mock_env)
    worldclock.convert_time()
    captured = capsys.readouterr()
    assert (
        captured.out == "CET                       03:30PM\n"
        "Australia/Sydney          12:30AM\n"
        "America/Los_Angeles       06:30AM\n"
    )


@freeze_time("2021-10-17 13:30:00")
def test_worldclock_args(monkeypatch, capsys):
    mock_env = {"TIMEZONE_LIST": '["CET", "Australia/Sydney", "America/Los_Angeles"]'}
    monkeypatch.setattr(os, "environ", mock_env)
    worldclock.convert_time(22, 55, "Europe/London")
    captured = capsys.readouterr()
    assert (
        captured.out == "CET                       11:55PM\n"
        "Australia/Sydney          08:55AM\n"
        "America/Los_Angeles       02:55PM\n"
    )
