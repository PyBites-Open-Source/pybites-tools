import argparse
import os
from pathlib import Path
import sys
import time

from dotenv import load_dotenv
from playsound import playsound

load_dotenv()

ALARM_MUSIC_FILE = os.environ["ALARM_MUSIC_FILE"]


def countdown_and_play_alarm(seconds: int, show_timer: bool = False) -> None:
    while seconds:
        mins, secs = divmod(seconds, 60)
        if show_timer:
            print(f"{mins:02}:{secs:02}", end="\r")
        time.sleep(1)
        seconds -= 1

    if show_timer:
        print("00:00", end="\r")
    playsound(ALARM_MUSIC_FILE)


def get_args():
    parser = argparse.ArgumentParser("Play an alarm after N minutes")
    parser.add_argument(
        "-m", "--minutes", required=True, help="Number of minutes to play alarm in"
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "-b",
        "--background",
        action="store_true",
        default=False,
        help="Run timer in the background",
    )
    group.add_argument(
        "-s",
        "--show_timer",
        action="store_true",
        default=False,
        help="Show timer in console",
    )
    return parser.parse_args()


def main(args=None):
    if args is None:
        args = get_args()

    minutes = int(args.minutes)
    if args.background:
        print(f"Playing alarm in {minutes} minute{'' if minutes == 1 else 's'}")

        package = __package__
        module = Path(sys.argv[0]).stem

        os.system(f"python -m {package}.{module} -m {minutes} &")
    else:
        seconds = minutes * 60
        try:
            countdown_and_play_alarm(seconds, show_timer=args.show_timer)
            sys.exit(0)
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    main()
