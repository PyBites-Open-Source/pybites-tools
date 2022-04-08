import argparse
import pytest

from pybites_tools.meaning import get_meaning, main
from unittest import mock


@pytest.mark.parametrize(
    "args, expected",
    [
        (
            argparse.Namespace(lang="en", origin=False, word="word"),
            "a single distinct meaningful element of speech or writing,",
        ),
        (
            argparse.Namespace(lang="en", origin=True, word="word"),
            "Old English, of Germanic origin; related to Dutch woord and German Wort, from an Indo-European root shared by Latin verbum ‘word’.",
        ),
    ],
)
def test_main(args, expected, capsys):
    main(args)
    captured = capsys.readouterr()
    assert expected in captured.out
