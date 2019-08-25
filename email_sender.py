#!/usr/bin/env python3
# coding: utf-8

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


def sendTextEmail(sender: str, receivers: list, mailConf: tuple,
                  subject: str = 'no subject',
                  text: str = 'no text') -> bool:
    '''[send plain text email]

    Args:
        sender: sender email address
        receivers: a list of receivers(str)
        mailConf: (mailHost, mailUser, mailPassword)
        subject: subject of this mail
    
    Returns:
        send successfully or not
    '''

    if len(mailConf) != 3:  # (host, user, password)
        return False
    host, user, password = mailConf

    message = MIMEText(text, 'plain', 'utf-8')
    message['From'] = sender
    message['To'] = ','.join(receivers)
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(host, 25)  # stmp port: 25
        smtpObj.login(user, password)
        smtpObj.sendmail(sender, receivers, message.as_string())
        return True
    except smtplib.SMTPException:
        return False
