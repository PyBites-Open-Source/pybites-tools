import argparse
import json
import os
from datetime import datetime, time

import pytz
from dotenv import load_dotenv
from pytz import timezone

FMT = "%I:%M%p"

load_dotenv()


def convert_a_given_time(hour, minute, user_tz):
    user_tz_now = datetime.now(timezone(f"{user_tz}"))
    user_given_time = user_tz_now.replace(hour=hour, minute=minute)
    formatted_dt = user_given_time.strftime(FMT)
    user_given_time_utc = user_given_time.astimezone(pytz.utc)

    print(f"Converting {formatted_dt} in {user_tz}:")

    try:
        timezones = json.loads(os.environ["TIMEZONE_LIST"])
        for zone in timezones:
            converted_time = user_given_time_utc.astimezone(pytz.timezone(zone))
            formatted_time = converted_time.strftime(FMT)
            print(f"{zone:25} {formatted_time}")
    except pytz.exceptions.UnknownTimeZoneError:
        print(
            "UnknownTimeZoneError occurred.  Please check your .env file for correct timezone names"
        )
    except json.decoder.JSONDecodeError as d:
        print("JSON error occurred.  Please check your .env file for syntax")
        print(d.args)


def convert_current_time():
    try:
        timezones = json.loads(os.environ["TIMEZONE_LIST"])
        for zone in timezones:
            converted_time = datetime.now(pytz.timezone(zone))
            formatted_time = converted_time.strftime(FMT)
            print(f"{zone:25} {formatted_time}")
    except pytz.exceptions.UnknownTimeZoneError:
        print(
            "UnknownTimeZoneError occurred.  Please check your .env file for correct timezone names"
        )
    except json.decoder.JSONDecodeError as d:
        print("JSON error occurred.  Please check your .env file for syntax")
        print(d.args)


def main():
    pass


if __name__ == "__main__":
    convert_current_time()
    print()
    convert_a_given_time(22, 22, "America/New_York")
