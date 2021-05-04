#!/usr/bin/env python3

#
# Class to send email.
# @author Tomasz Zymni <tomasz.zymni@gmail.com>
#
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

import yaml

# Load configuration from yaml file.
def LoadConfig():
    global config

    with open("config.yaml", "r") as yamlfile:
        config = yaml.load(yamlfile, Loader=yaml.FullLoader)


class EmailSender:

    def __init__(self):
        LoadConfig()

    # Send email based on configuration with file attached in parameter.
    def SendMail(self, ImgFileName):
        img_data = open(ImgFileName, 'rb').read()
        msg = MIMEMultipart()

        msg['Subject'] = config["email"]['subject']
        msg['From'] = config["email"]['from']
        msg['To'] = config["email"]['to']

        text = MIMEText(config["email"]['message'])
        msg.attach(text)
        image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
        msg.attach(image)

        s = smtplib.SMTP(config["smtp"]['host'], config["smtp"]['port'])
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(config["smtp"]['user'], config["smtp"]['password'])
        s.sendmail(config["email"]['from'], config["email"]['to'], msg.as_string())
        s.quit()


