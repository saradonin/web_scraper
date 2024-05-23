import smtplib
import os
from dotenv import load_dotenv, find_dotenv
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

load_dotenv(find_dotenv())


def generate_email_content(items):

    list_items_html = ''.join(
        f'<li>{item["name"]} - {item["price"]} - <a href="{item["link"]}">LINK</a></li>' for item in items)

    html_content = f"""
    <!DOCTYPE html>
    <html>
        <head>
            <title>New items in stock!</title>
        </head>
        <body>
            <h1>New items available:</h1>
            <ul>
                {list_items_html}
            </ul>
            <br>
            <p>Email sent from Web Scrapper App by saradonin</p>
        </body>
    </html>
    """
    return html_content


def send_email(list):

    sender_email = os.environ.get("EMAIL_LOGIN")
    sender_password = os.environ.get("EMAIL_PASSWORD")
    receiver_emails = os.environ.get("EMAIL_RECIPENTS").split(',')

    html_content = generate_email_content(list)

    # Initialize the SMTP server
    server = smtplib.SMTP_SSL('smtp.googlemail.com', 465)
    server.login(sender_email, sender_password)

    for receiver_email in receiver_emails:
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "New items in stock"
        msg['From'] = sender_email
        msg['To'] = receiver_email

        # Attach the HTML content
        msg.attach(MIMEText(html_content, 'html'))
        # Send the email
        server.sendmail(sender_email, receiver_email, msg.as_string())

    server.quit()
    print("Email sent successfully.")
