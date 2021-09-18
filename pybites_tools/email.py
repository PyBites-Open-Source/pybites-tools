import argparse
import os
import ssl
import smtplib
from typing import Optional

from dotenv import load_dotenv

load_dotenv()


class MissingRecipientEmail(Exception):
    """Exception to be raised if no recipient email is provided"""


def send_email(subject: str, message: str, to_email: Optional[str] = None) -> None:
    """
    Send an email message. Retrieve config from environment. If to_email is not
    provided try sending it to EMAIL_DEFAULT_TO_EMAIL.
    """
    host = os.environ["EMAIL_SMTP_HOST"]
    port = int(os.environ.get("EMAIL_SMTP_PORT", 587))
    from_email = os.environ["EMAIL_USERNAME"]
    password = os.environ["EMAIL_PASSWORD"]
    to_email = to_email or os.environ.get("EMAIL_DEFAULT_TO_EMAIL")

    if to_email is None:
        raise MissingRecipientEmail("Need to specify a recipient email")

    context = ssl.create_default_context()

    with smtplib.SMTP(host, port) as server:
        server.starttls(context=context)
        server.login(from_email, password)

        email_message = f"Subject: {subject}\n\n{message}"
        server.sendmail(from_email, to_email, email_message)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--subject", required=True)
    parser.add_argument("-m", "--message", required=True)
    parser.add_argument("-e", "--email")

    args = parser.parse_args()
    send_email(args.subject, args.message, args.email)


if __name__ == "__main__":
    main()
