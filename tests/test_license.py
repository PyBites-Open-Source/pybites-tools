import re

import pytest

from pybites_tools.license import generate_license_key


@pytest.mark.parametrize(
    "parts, chars_per_part, separator, pat",
    [
        (4, 8, "-", re.compile(r"^([A-Z0-9]{8}-){3}[A-Z0-9]{8}$")),
        (2, 8, "-", re.compile(r"^[A-Z0-9]{8}-[A-Z0-9]{8}$")),
        (4, 6, "-", re.compile(r"^([A-Z0-9]{6}-){3}[A-Z0-9]{6}$")),
        (4, 8, "`", re.compile(r"^([A-Z0-9]{8}`){3}[A-Z0-9]{8}$")),
        (1, 2, "¡", re.compile(r"^[A-Z0-9]{2}$")),
        (4, 2, ":", re.compile(r"^([A-Z0-9]{2}:){3}[A-Z0-9]{2}$")),
    ],
)
def test_generate_license_key(parts, chars_per_part, separator, pat):
    assert pat.match(generate_license_key(parts, chars_per_part, separator))
