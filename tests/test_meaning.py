import argparse
import pytest

from pybites_tools.meaning import get_meaning, main
from unittest import mock


@pytest.mark.parametrize(
    "args, expected",
    [
        (
            argparse.Namespace(origin=False, word="word"),
            "The smallest unit of language that has a particular meaning and can be expressed by itself; the smallest discrete, meaningful unit of language. (contrast morpheme.)",
        ),
        (
            argparse.Namespace(origin=True, word="word"),
            "No origin information available",
        ),
    ],
)
def test_main(args, expected, capsys):
    main(args)
    captured = capsys.readouterr()
    assert expected in captured.out
