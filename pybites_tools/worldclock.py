import json
import os
from datetime import datetime
from zoneinfo import ZoneInfo

from dotenv import load_dotenv
import pytz

load_dotenv()


def main():
    try:
        timezones = json.loads(os.environ["TIMEZONE_LIST"])
        for zone in timezones:
            zone_now = datetime.now(pytz.timezone(zone))
            formatted_time = zone_now.strftime("%I:%M%p")
            print(f"{zone:25} {formatted_time}")
    except pytz.exceptions.UnknownTimeZoneError:
        print(
            "UnknownTimeZoneError occurred.  Please check your .env file for correct timezone names"
        )
    except json.decoder.JSONDecodeError as d:
        print("JSON error occurred.  Please check your .env file for syntax")
        print(d.args)


if __name__ == "__main__":
    main()
