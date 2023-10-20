import argparse

import pytest

from pybites_tools.meaning import get_meaning, main


@pytest.mark.parametrize(
    "args, expected",
    [
        (
            argparse.Namespace(word="fish", lang=["en"]),
            "any of a large group of cold-blooded aquatic vertebrates having jaws",
        ),
        (
            argparse.Namespace(word="Fisch", lang=["de"]),
            "ein im Wasser lebendes Wirbeltier, das eine mit Schuppen bedeckte Haut hat, mit Kiemen atmet und Flossen zum Schwimmen besitzt",
        ),
    ],
)
def test_main(args, expected, capsys):
    main(args)
    captured = capsys.readouterr()
    print(captured.out)
    assert expected in captured.out


@pytest.mark.parametrize(
    "word, site, datasrc, expected",
    [
        (
            "fish",
            "https://www.thefreedictionary.com/",
            {"data-src": "hc_dict"},
            "any of a large group of cold-blooded aquatic vertebrates having jaws",
        ),
        (
            "Fisch",
            "https://de.thefreedictionary.com/",
            {"data-src": "pons"},
            "ein im Wasser lebendes Wirbeltier, das eine mit Schuppen bedeckte Haut hat, mit Kiemen atmet und Flossen zum Schwimmen besitzt",
        ),
    ],
)
def test_get_meaning(word, site, datasrc, expected):
    response = get_meaning(word, site, datasrc)
    print(response)
    assert expected in response
