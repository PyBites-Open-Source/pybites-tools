import sys
from io import StringIO


def zen_of_python() -> list[str]:
    """
    Dump the Zen of Python into a variable
    https://stackoverflow.com/a/23794519
    """
    zen = StringIO()
    old_stdout = sys.stdout
    sys.stdout = zen
    import this

    sys.stdout = old_stdout
    return zen.getvalue().splitlines()
