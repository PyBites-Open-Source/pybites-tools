import argparse
import json
import os
from datetime import datetime
import sys

import pytz
from dotenv import load_dotenv
from pytz import timezone

DEFAULT_FMT = "%I:%M%p"
DEFAULT_TIMEZONE = "UTC"

load_dotenv()


class WorldClockException(Exception):
    pass


def convert_time(hour: int = None, minute: int = None, tzone: str = None) -> None:
    try:
        timezones = json.loads(os.environ["TIMEZONE_LIST"])
    except json.decoder.JSONDecodeError:
        raise WorldClockException(
            "JSON error occurred. Please check your .env file for syntax"
        )

    for zone in timezones:
        try:
            if hour in range(0, 23):
                user_given_tz_now = datetime.now(timezone(f"{tzone}"))
                user_given_time = user_given_tz_now.replace(hour=hour, minute=minute)
                user_given_time_utc = user_given_time.astimezone(pytz.utc)
                converted_time = user_given_time_utc.astimezone(pytz.timezone(zone))
            else:
                converted_time = datetime.now(pytz.timezone(zone))
        except pytz.exceptions.UnknownTimeZoneError:
            raise WorldClockException(
                "UnknownTimeZoneError - Check that your timezones are spelled correctly."
            )

        FMT = os.getenv("TIME_FORMAT", DEFAULT_FMT)
        formatted_time = converted_time.strftime(FMT)
        print(f"{zone:25} {formatted_time}")


def main():
    now = datetime.now()

    parser = argparse.ArgumentParser()
    parser.add_argument("-hr", "--hour", type=int, default=now.hour)
    parser.add_argument("-min", "--minute", type=int, default=now.minute)
    parser.add_argument("-tz", "--tzone", type=str, default=DEFAULT_TIMEZONE)

    args = parser.parse_args()
    try:
        convert_time(args.hour, args.minute, args.tzone)
    except WorldClockException as exc:
        print(exc)
        sys.exit(1)


if __name__ == "__main__":
    main()
