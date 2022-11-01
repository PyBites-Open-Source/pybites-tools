import argparse
import requests

from bs4 import BeautifulSoup as bs4
from requests.exceptions import HTTPError


def get_meaning(word, site, datasrc):

    try:
        response = requests.get(site + word)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        exit(255)
    except Exception as err:
        print(f"Other error occurred: {err}")
        exit(255)

    soup = bs4(response.text, "html.parser")

    data = soup.find("section", attrs=datasrc).findAll("div")

    meaning = ""
    for line in data:
        meaning = f"{meaning}\n{line.get_text()}"

    return meaning


def main(args):

    word = args.word

    if args.lang == ["en"]:
        intro = "Your word was"
        datasrc = {"data-src": "hc_dict"}
        site = "https://www.thefreedictionary.com/"

    if args.lang == ["de"]:
        intro = "Dein Wort war"
        datasrc = {"data-src": "pons"}
        site = "https://de.thefreedictionary.com/"

    meaning = get_meaning(word, site, datasrc)

    print(f"{intro}: {word}\n\t{meaning}")


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

    main(args)
