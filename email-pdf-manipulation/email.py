#!/usr/bin/env python3
from email.message import EmailMessage
import os.path, mimetypes, smtplib, getpass

def sendemail():
    sender = "me@example.com"
    recipient = "you@example.com"
    body = """Hey there!
    ...
    ... I'm learning to send emails using Python!"""
    attachment_path = "/tmp/example.png"

    attachment_filename = os.path.basename(attachment_path)
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split('/', 1)

    message = EmailMessage()

    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = 'Greetings from {} to {}!'.format(sender, recipient)
    message.set_content(body)

    with open(attachment_path, 'rb') as ap:
      message.add_attachment(ap.read(),maintype=mime_type,subtype=mime_subtype,filename=os.path.basename(attachment_path))
    
    mail_server = smtplib.SMTP_SSL('smtp.example.com')
    mail_pass = getpass.getpass('Password? ')

    # If you want to see the SMTP messages that are being sent back and forth by the smtplib module behind the scenes
    # mail_server.set_debuglevel(1)

    # login
    mail_server.login(sender, mail_pass)
    # this the feedback for login tuple (235, b'2.7.0 Accepted')

    # send
    mail_server.send_message(message)
    # feedback empty {}

    # quit
    mail_server.quit()


