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
    import this  # noqa F401

    sys.stdout = old_stdout
    return zen.getvalue().splitlines()


def main():
    import pyperclip

    zen = "\n".join(zen_of_python())
    pyperclip.copy(zen)
    print("The Zen of Python has been copied to your clipboard")


if __name__ == "__main__":
    main()
