import argparse
import json
import os
import sys
from datetime import datetime

from dateutil import tz
from dotenv import load_dotenv

DEFAULT_FMT = "%I:%M%p"
DEFAULT_TIMEZONE = "UTC"
HOURS_IN_DAY = range(0, 24)
MINUTES_IN_HOUR = range(0, 60)
MONTHS_IN_YEAR = range(1, 13)
MAX_DAYS_IN_MONTH = range(1, 32)

load_dotenv()


class WorldClockException(Exception):
    pass


def convert_time(
    hour: int = None,
    minute: int = None,
    year: int = None,
    month: int = None,
    day: int = None,
    tzone: str = None,
    date_offset: bool = False,
) -> None:
    try:
        timezones = json.loads(os.environ["TIMEZONE_LIST"])
    except json.decoder.JSONDecodeError:
        raise WorldClockException(
            "JSON error occurred. Please check your .env file for syntax"
        )

    for zone in timezones:
        if tz.gettz(zone) is None:
            raise WorldClockException(
                "UnknownTimeZoneError - Check that your timezones are spelled correctly."
            )
        if (
            hour in HOURS_IN_DAY
            and minute in MINUTES_IN_HOUR
            and month in MONTHS_IN_YEAR
            and day in MAX_DAYS_IN_MONTH
        ):
            user_given_tz_now = datetime.now(tz.gettz(tzone))
            user_given_time = user_given_tz_now.replace(
                hour=hour, minute=minute, year=year, month=month, day=day
            )
            user_given_time_utc = user_given_time.astimezone(tz.UTC)
            converted_time = user_given_time_utc.astimezone(tz.gettz(zone))
        else:
            converted_time = datetime.now(tz.gettz(zone))

        FMT = os.getenv("TIME_FORMAT", DEFAULT_FMT)
        formatted_time = converted_time.strftime(FMT)

        if date_offset:
            formatted_time += f"   {converted_time.strftime('%d %b %Y')}"

        print(f"{zone:25} {formatted_time}")


def main():
    now = datetime.now()

    # override DEFAULT_TIMEZONE if TIMEZONE is present in .env
    timezone = os.getenv("TIMEZONE", DEFAULT_TIMEZONE)

    parser = argparse.ArgumentParser()
    parser.add_argument("-hr", "--hour", type=int, default=now.hour)
    parser.add_argument("-min", "--minute", type=int, default=now.minute)
    parser.add_argument("-y", "--year", type=int, default=now.year)
    parser.add_argument("-m", "--month", type=int, default=now.month)
    parser.add_argument("-d", "--day", type=int, default=now.day)
    parser.add_argument("-tz", "--tzone", type=str, default=timezone)
    parser.add_argument("-do", "--date-offset", action="store_true")

    args = parser.parse_args()
    try:
        print(f"args: {args}")
        convert_time(
            args.hour,
            args.minute,
            args.year,
            args.month,
            args.day,
            args.tzone,
            args.date_offset,
        )
    except WorldClockException as exc:
        print(exc)
        sys.exit(1)


if __name__ == "__main__":
    main()
