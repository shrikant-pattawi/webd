# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python

import sendgrid
import os
from sendgrid.helpers.mail import *


#API_KEY=""

# def send_mail(to, subject, content):
# 	sg = sendgrid.SendGridAPIClient("")
# 	from_email = Email("webd <sahaj@mnnit.ac.in>")
# 	to_email = Email(to)
# 	content = Content("text/html", content)
# 	mail = Mail(from_email, subject, to_email, content)
# 	response = sg.client.mail.send.post(request_body=mail.get())


import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_mail(to, subject, content):
    message = Mail(
        from_email='sahaj@mnnit.ac.in',
        to_emails=to,
        subject=subject,
        html_content=content)
    try:
        sg = SendGridAPIClient(os.environ.get(''))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)