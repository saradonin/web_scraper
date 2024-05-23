import smtplib
import os
from dotenv import load_dotenv, find_dotenv
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

load_dotenv(find_dotenv())



def send_email(list):
    
    list_items_html = ''.join(f'<li>{item["name"]} - {item["price"]} PLN - <a href={item["link"]}>LINK</a></li>' for item in list)
    
    sender_email = os.environ.get("EMAIL_LOGIN")
    sender_password = os.environ.get("EMAIL_PASSWORD")
    
    # Initialize the SMTP server
    server = smtplib.SMTP_SSL('smtp.googlemail.com', 465)
    server.login(sender_email, sender_password)
    receiver_emails = ["michalkdp@tlen.pl"]

    for receiver_email in receiver_emails:
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "New items in stock"
        msg['From'] = sender_email
        msg['To'] = receiver_email
        
        html_content = f"""
    <h1>New items:</h1>
    <ul>
    {list_items_html}
    </ul>
"""
        # Attach the HTML content
        msg.attach(MIMEText(html_content, 'html'))
        # Send the email
        server.sendmail(sender_email, receiver_email, msg.as_string())

    server.quit()

