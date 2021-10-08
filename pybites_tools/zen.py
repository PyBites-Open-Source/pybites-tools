from contextlib import redirect_stdout
from io import StringIO


def zen_of_python():
    input = StringIO()
    with redirect_stdout(input):
        import this
    zen = input.getvalue()

    return zen


def main():
    import pyperclip

    zen = zen_of_python()
    pyperclip.copy(zen)
    print("The Zen of Python has been copied to your clipboard")


if __name__ == "__main__":
    main()
