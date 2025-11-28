import smtplib
import ssl
from email.message import EmailMessage

EMAIL = "EMAIL"
APP_PASSWORD = "APP_PASSWORD"
RECEIVER = "receiver@gmail.com"

msg = EmailMessage()
msg["From"] = EMAIL
msg["To"] = RECEIVER
msg["Subject"] = "Hello from Python........."
msg.set_content("This email was shared by python code.....")

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(EMAIL, APP_PASSWORD)
    server.send_message(msg)
