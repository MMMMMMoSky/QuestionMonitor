#!/usr/bin/env python3
# coding: utf-8

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


def sendTextEmail(sender: str, receivers: list, mailConf: tuple,
                  subject: str = 'no subject',
                  text: str = 'no text') -> bool:
    '''
    [send plain text email]
    @param sender: sender email address
    @param receivers: a list of receivers(str)
    @param mailConf: (mailHost, mailUser, mailPassword)
    @param subject: subject of this mail
    @return: send successfully or not
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
