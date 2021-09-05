import os
import shutil
import ssl
import smtplib

from dotenv import load_dotenv

load_dotenv()


def send_email(to_email: str, subject: str, message: str) -> None:
    """
    Send an email message using environment settings.
    """
    host = os.environ["EMAIL_SMTP_HOST"]
    port = os.environ.get("EMAIL_SMTP_PORT", 587)
    from_email = os.environ["EMAIL_USERNAME"]
    password = os.environ["EMAIL_PASSWORD"]

    context = ssl.create_default_context()
    email_message = f"Subject: {subject}\n\n{message}"
    with smtplib.SMTP(host, port) as server:
        server.starttls(context=context)
        server.login(from_email, password)
        server.sendmail(from_email, to_email, email_message)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--subject", required=True)
    parser.add_argument("-m", "--message", required=True)
    args = parser.parse_args()
