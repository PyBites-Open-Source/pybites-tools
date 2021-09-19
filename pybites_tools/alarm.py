import argparse
import os
import time

from dotenv import load_dotenv
from playsound import playsound

load_dotenv()

ALARM_MUSIC_FILE = os.environ["ALARM_MUSIC_FILE"]


def countdown(seconds: int) -> None:
    while seconds:
        mins, secs = divmod(seconds, 60)
        print(f"{mins:02}:{secs:02}", end="\r")
        time.sleep(1)
        seconds -= 1

    print("00:00", end="\r")
    playsound(ALARM_MUSIC_FILE)


def main():
    parser = argparse.ArgumentParser("Play an alarm after N minutes")
    parser.add_argument(
        "-m", "--minutes", required=True, help="Number of minutes to countdown from"
    )
    args = parser.parse_args()
    seconds = int(args.minutes) * 60
    try:
        countdown(seconds)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
