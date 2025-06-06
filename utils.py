# utils.py

from datetime import datetime
import pytz
import logging


def logging_config():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s %(message)s]",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[logging.StreamHandler(), logging.FileHandler("app.log", mode="a")],
    )


def egypt_timezone() -> str:
    """
    Returns the current date and time in the Egypt timezone ("Africa/Cairo")
    formatted as an ISO 8601 string including seconds, e.g. '2025-06-06T14:45:30+02:00'.

    Returns:
        str: ISO formatted datetime string localized to Egypt time.
    """
    # Create a timezone object for Africa/Cairo (Egypt)
    egypt_tz = pytz.timezone("Africa/Cairo")

    # Get the current time localized to Egypt timezone
    now_in_egypt = datetime.now(egypt_tz)

    # Convert the datetime to ISO 8601 string including seconds (no microseconds)
    # The output includes timezone offset like '+02:00' for clarity
    iso_timestamp = now_in_egypt.isoformat(timespec="seconds")

    return iso_timestamp
