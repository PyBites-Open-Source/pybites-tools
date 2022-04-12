import argparse
import requests


def get_meaning(args):
    word = args.word

    request = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

    response = requests.get(request)

    if response.status_code == 404:
        return "No definitions found for that word, please check your spelling"

    if response.status_code != 200:
        return "Something went wrong on the server side"

    data = response.json()

    if "origin" in data[0]:
        origin = data[0]["origin"]
    else:
        origin = "No origin information available"

    meanings = f"Your word was: {word}"
    if args.origin:
        meanings = meanings + f"\nThe origin of the word is:-\n{origin}"
    for meaning in data[0]["meanings"]:
        meanings = meanings + "\n" + meaning["partOfSpeech"]
        for definition in meaning["definitions"]:
            meanings = meanings + "\n\t" + definition["definition"]
            if "example" in definition:
                meanings = meanings + "\n\t\t" + definition["example"]

    return meanings


def main(args):
    print(get_meaning(args))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("word", help="The word you want to know the meaning of")
    parser.add_argument(
        "-o",
        "--origin",
        action="store_true",
        help="return the origin of the word requested",
    )

    args = parser.parse_args()

    main(args)
