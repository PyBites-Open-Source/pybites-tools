import argparse

import requests


def get_meaning(args):
    lang = "en"
    word = args.word

    if args.lang:
        lang = args.lang

    request = f"https://api.dictionaryapi.dev/api/v2/entries/{lang}/{word}"

    response = requests.get(request)

    if response.status_code == 404:
        return "No Definitions Found"

    if response.status_code != 200:
        return "Something went wrong on the server side"

    data = response.json()

    origin = data[0]["origin"]
    meanings = ""
    for meaning in data[0]["meanings"]:
        print(meaning)

    return origin


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("word", help="The word you want to know the meaning of")
    parser.add_argument(
        "-l",
        "--lang",
        help="Set the language for the word in ISO 2 letter format. For more information see https://www.sitepoint.com/iso-2-letter-language-codes/",
    )

    args = parser.parse_args()
    print(get_meaning(args))


if __name__ == "__main__":
    main()
