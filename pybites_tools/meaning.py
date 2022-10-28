import argparse
import urllib.request as r
import urllib.error

from bs4 import BeautifulSoup as bs4


def get_meaning(word, site, datasrc):

    try:
        response = r.urlopen(site + word).read().decode()
    except urllib.error.HTTPError as e:
        print(
            f"Error getting url. Please check to see if you can access {site}{word} in a browser"
        )
        exit(1)

    soup = bs4(response, "html.parser")

    data = soup.find("section", attrs=datasrc).findAll("div")

    meaning = ""
    for line in data:
        meaning = f"{meaning}\n{line.get_text()}"

    return meaning


def main(args):

    word = args.word

    print(args.lang)
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
