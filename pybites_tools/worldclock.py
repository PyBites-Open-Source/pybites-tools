import json
import os
from datetime import datetime
from zoneinfo import ZoneInfo

from dotenv import load_dotenv

load_dotenv()


def main():
    timezones = json.loads(os.environ["TIMEZONE_LIST"])
    for zone in timezones:
        zone_now = datetime.now(ZoneInfo(zone))
        formatted_time = zone_now.strftime("%I:%M%p")
        print("{0:25} {1}".format(zone, formatted_time))


if __name__ == "__main__":
    main()
