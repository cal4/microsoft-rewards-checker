import os
import smtplib
import ssl
from email.message import EmailMessage

from dotenv import load_dotenv


def pytest_sessionfinish(session, exitstatus):
    """
    Called after whole test run finished, right before
    returning the exit status to the system.
    """
    if exitstatus == 0:
        return

    load_dotenv()

    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = os.getenv("FROM_EMAIL")
    email_message = EmailMessage()
    email_message["Subject"] = str(session)
    email_message["To"] = os.getenv("TO_EMAIL")
    email_message.set_content(str(session.items))

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, os.getenv("PASSWORD"))
        server.send_message(email_message)
