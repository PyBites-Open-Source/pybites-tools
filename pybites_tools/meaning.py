import argparse
import sys
from urllib.error import HTTPError

import requests
from bs4 import BeautifulSoup as bs4


class MeaningError(Exception):
    pass


SUCCESS, FAILURE = 0, 255


def get_meaning(word: str, site: str, datasrc: dict) -> str:
    try:
        response = requests.get(site + word)
        response.raise_for_status()
    except HTTPError as error:
        error_msg = (
            "Word not found"
            if error.code == requests.codes.not_found
            else f"An error occurred: {error}"
        )
        raise MeaningError(error_msg)

    soup = bs4(response.text, "html.parser")

    data = soup.find("section", attrs=datasrc).findAll("div")

    meaning = ""
    for line in data:
        meaning = f"{meaning}\n{line.get_text()}"

    return meaning


def main(args) -> int:
    word = args.word

    if args.lang == ["en"]:
        intro = "Your word was"
        datasrc = {"data-src": "hc_dict"}
        site = "https://www.thefreedictionary.com/"

    if args.lang == ["de"]:
        intro = "Dein Wort war"
        datasrc = {"data-src": "pons"}
        site = "https://de.thefreedictionary.com/"

    try:
        meaning: str = get_meaning(word, site, datasrc)
    except MeaningError:
        return FAILURE

    print(f"{intro}: {word}\n\t{meaning}")

    return SUCCESS


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("word", help="The word you want to know the meaning of")
    parser.add_argument(
        "-l",
        "--lang",
        nargs=1,
        help="Select a language. en is default DE is an option",
        type=str,
        choices=["en", "de"],
        default=["en"],
    )

    args = parser.parse_args()

    sys.exit(main(args))
