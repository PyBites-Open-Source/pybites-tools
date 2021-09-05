import os
import ssl
import smtplib

from dotenv import load_dotenv

load_dotenv()

EMAIL_SMTP_HOST = os.environ["EMAIL_SMTP_HOST"]
EMAIL_SMTP_PORT = os.environ.get("EMAIL_SMTP_PORT", 587)
EMAIL_USERNAME = os.environ["EMAIL_USERNAME"]
EMAIL_PASSWORD = os.environ["EMAIL_PASSWORD"]


def send_email(to_email: str, subject: str, message: str) -> None:
    """
    Send an email message.
    """
    context = ssl.create_default_context()
    email_message = f"Subject: {subject}\n\n{message}"
    with smtplib.SMTP(EMAIL_SMTP_HOST, EMAIL_SMTP_PORT) as server:
        server.starttls(context=context)
        server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
        server.sendmail(EMAIL_USERNAME, to_email, email_message)
