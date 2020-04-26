import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Dict


def send_email(
        email_from: str,
        password: str,
        email_to: str,
        message: Dict[str, str]
) -> None:
    msg = MIMEMultipart()
    msg['From'] = email_from
    msg['To'] = email_to
    msg['Subject'] = message.get('subject')
    message = message.get('message')
    msg.attach(MIMEText(message))
    mail_server = smtplib.SMTP('poczta.o2.pl', 587)
    mail_server.login(email_from, password)
    mail_server.sendmail(email_from, email_to, msg.as_string())
    mail_server.quit()
