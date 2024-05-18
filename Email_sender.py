from email.message import EmailMessage
from app2 import password
import ssl
import smtplib

email_sender = 'fung403@gmail.com'
email_password = password

email_receiver ='fung.chan@outlook.com'

subject = "Hello! This email by Python email sender."
body = "When you are watching my project, pleae feel free to give comments. Hope you have a good day!"

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())