from secrets import choice
from string import ascii_uppercase, digits

ALPHABET = ascii_uppercase + digits


def generate_license_key(
    parts: int = 4, chars_per_part: int = 8, separator: str = "-"
) -> str:
    """
    Generate a license key of N parts.

    For example with the default arguments you would get a string like this:
    UT40MFLM-WF7R0X7M-NCDKGMD4-D80A3M8R
    """
    return separator.join(
        "".join(choice(ALPHABET) for i in range(chars_per_part)) for _ in range(parts)
    )
