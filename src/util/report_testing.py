import os
import boto3
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_testing_result_to_the_slack_channel():
    msg = MIMEMultipart()
    msg["Subject"] = "Data testing "+ os.environ["SNOWFLAKE_SCHEMA"] +" automation test notification"
    msg["From"] = os.environ["DATA_OPS_EMAIL"]
    msg["To"] = os.environ["DATA_OPS_EMAIL"]

    # Set message body
    body = MIMEText("""
    Data testing automation test notification. 
    The report is attached with the mail.
    """, "plain")
    msg.attach(body)

    filename = "pytest_reports/pytest_html_report.html"  # In same directory as script

    with open(filename, "rb") as attachment:
        part = MIMEApplication(attachment.read())
        part.add_header("Content-Disposition",
                        "attachment",
                        filename=filename)
    msg.attach(part)

    # Convert message to string and send
    ses_client = boto3.client("ses", region_name="us-east-1")
    response = ses_client.send_raw_email(
        Source=msg["From"],
        Destinations=[msg["To"]],
        RawMessage={"Data": msg.as_string()}
    )
    print(response)

send_testing_result_to_the_slack_channel()
   