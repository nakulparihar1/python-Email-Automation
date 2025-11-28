# 📧 Email Automation using Python

This project demonstrates how to send emails automatically using Python, SMTP, and SSL encryption. It creates an email with a subject and message body, connects securely to Gmail’s SMTP server, logs in using an App Password, and sends the email to a specified recipient.

🚀 Features

Send emails automatically using Python

Secure connection with SSL

Supports custom subject and message

Works with Gmail App Password

📦 Requirements

Install Python and required library (already built-in):

pip install secure-smtplib


Note: smtplib, ssl, and email.message come pre-installed with Python.

🔐 Security Note

Never share your real email password. Use a Gmail App Password instead.
Also, do not upload your credentials to GitHub.

Use environment variables:

Windows (PowerShell)
setx EMAIL "your_email@gmail.com"
setx APP_PASSWORD "your_app_password"

Mac / Linux
export EMAIL="your_email@gmail.com"
export APP_PASSWORD="your_app_password"

▶️ How to Run

Set environment variables (EMAIL and APP_PASSWORD)

Save the file as email_sender.py

Run the program:

python email_sender.py


Email will be sent instantly ✅
