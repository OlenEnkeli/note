import smtplib

from config import config


def send_mail(subject, to, text):

    server = smtplib.SMTP(config['email']['host'])
    server.starttls()
    server.login(config['email']['user'], config['email']['password'])

    body = (
        "From: " + config['email']['from'] + "\r\n" +
        "To: " + ','.join(to) + "\r\n" +
        "Subject: " + subject + "\r\n"*2 +
        text
    )

    server.sendmail(config['email']['from'], to, body)
    server.quit()
