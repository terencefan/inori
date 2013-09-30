# -*- coding: utf-8 -*-

import smtplib
from email.MIMEText import MIMEText


class MailBase():

    def __init__(self, username, password):

        self.username = username
        self.smtp = smtplib.SMTP()

        try:
            error = 'CONNECT REFUSED'
            self.smtp.connect(self.SMTP_HOST, self.SMTP_PORT)
            self.smtp.starttls()
            error = 'LOGIN REFUSED'
            self.smtp.login(username, password)
        except:
            print "EMAIL INIT FAILED ({}) ******".format(error)

    def send(self, to_email, title, content):

        # FIXME unicode encode
        if isinstance(title, unicode):
            title = title.encode('utf-8')

        msg = MIMEText(title)
        msg['From'] = self.username
        msg['To'] = to_email
        msg['Subject'] = content

        try:
            self.smtp.sendmail(self.username, to_email, msg.as_string())
            return True
        except:
            return False


class GMail(MailBase):

    SMTP_HOST = 'smtp.gmail.com'
    SMTP_PORT = 25
