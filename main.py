import smtplib
import ssl
from ssl import SSLContext
from threading import Thread
from smtplib import SMTP_SSL
from concurrent.futures import ThreadPoolExecutor
from email.mime.text import MIMEText

# Configuration
port = 465
smtp_server = "gnldm1070.siteground.biz"
login = "test@webhoch.com"  # Your login generated by Mailtrap
password = "y4E4-11@m#1"  # Your password generated by Mailtrap

sender_email = "test@webhoch.com"
receiver_email = "stevanvlajic5@gmail.com"

# Plain text content
text = """\
Hi,
Check out the new post on the Mailtrap blog:
SMTP Server for Testing: Cloud-based or Local?
https://blog.mailtrap.io/2018/09/27/cloud-or-local-smtp-server/
Feel free to let us know what content would be useful for you!
"""

# Create MIMEText object
message = MIMEText(text, "plain")
message["Subject"] = "Plain text email"
message["From"] = sender_email
message["To"] = receiver_email

context = ssl.create_default_context()

import random
import string

def generate_random_email():
    # Generate a random string of lowercase letters
    random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(8))
    # Append a random domain
    domain = random.choice(['example.com', 'test.org', 'demo.net'])
    # Return the random email
    return f"{random_string}@{domain}"

# Generate 30 non-existing emails
non_existing_emails = [generate_random_email() for _ in range(30)]
non_existing_emails.append('stevanvlajic.business@gmail.com')

# Print the list of non-existing emails
for email in non_existing_emails:
    print(email)


def send_mail(mail):
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, mail, message.as_string())

    
with ThreadPoolExecutor() as executor:
    executor.map(send_mail, non_existing_emails)