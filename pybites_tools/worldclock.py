import argparse
import json
import os
from datetime import datetime
import sys

import pytz
from dotenv import load_dotenv
from pytz import timezone

FMT = "%I:%M%p"

load_dotenv()


def convert_time(hour=None, minute=None, tzone=None):
    try:
        timezones = json.loads(os.environ["TIMEZONE_LIST"])
    except json.decoder.JSONDecodeError as d:
        print("JSON error occurred.  Please check your .env file for syntax")
        sys.exit(d.args)

    for zone in timezones:
        try:
            if not hour:
                converted_time = datetime.now(pytz.timezone(zone))
                formatted_time = converted_time.strftime(FMT)
                print(f"{zone:25} {formatted_time}")
            else:
                user_given_tz_now = datetime.now(timezone(f"{tzone}"))
                user_given_time = user_given_tz_now.replace(hour=hour, minute=minute)
                user_given_time_utc = user_given_time.astimezone(pytz.utc)
                converted_time = user_given_time_utc.astimezone(pytz.timezone(zone))
                formatted_time = converted_time.strftime(FMT)
                print(f"{zone:25} {formatted_time}")
        except pytz.exceptions.UnknownTimeZoneError:
            sys.exit(
                "UnknownTimeZoneError - Check that your timezones are spelled correctly."
            )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-hr", "--hour", type=int)
    parser.add_argument("-min", "--minute", type=int)
    parser.add_argument("-tz", "--tzone", type=str)

    args = parser.parse_args()
    convert_time(args.hour, args.minute, args.tzone)


if __name__ == "__main__":
    main()
