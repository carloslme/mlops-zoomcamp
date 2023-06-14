import os

from dotenv import load_dotenv, find_dotenv
from prefect_email import EmailServerCredentials


load_dotenv(find_dotenv())
gmail = os.getenv("MAIL")
app_gmail_password = os.getenv("PASS_APP_GMAIL")
email_name = os.getenv("EMAIL_NAME")

credentials = EmailServerCredentials(
    username=gmail,
    password=app_gmail_password,  # must be an app password
)
credentials.save(email_name)