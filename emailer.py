import smtplib
import configuration
from email.message import EmailMessage

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    user = configuration.email_username
    password = configuration.email_password
    msg['from'] = user
    server = smtplib.SMTP(configuration.email_server_name, configuration.email_server_port)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()


