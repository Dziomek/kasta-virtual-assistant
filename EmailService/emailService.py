from EmailService.emailConfig import EMAIL_ADDRESS
from EmailService.emailConfig import EMAIL_PASSWORD
import smtplib
from email.message import EmailMessage
import codecs

from jinja2 import  Environment, FileSystemLoader


class MailService:
    def __init__(self):
        #with smtplib.SMTP_SSL('smtp.gmail.com', 465) as self.smtp:
         #   self.smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        self.smtpObj = smtplib.SMTP("smtp.gmail.com",587)
        self.smtpObj.ehlo()
        self.smtpObj.starttls()
        self.smtpObj.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    def emailVerification(self,
                          firstName,
                          lastName,
                          emailUser,
                          token):
        msg = EmailMessage()
        msg['Subject'] = 'Kasta VA: Account verification'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = emailUser

        username = firstName
        email = emailUser
        token = token

        file_loader = FileSystemLoader('EmailService/templates')
        env = Environment(loader=file_loader)
        template = env.get_template('emailVerification.html')
        output = template.render(email=email, username=username, token=token)
        msg.add_alternative(output, subtype='html')

        self.smtpObj.send_message(msg)


    def sendNoteViaEmail(self,firstName, emailUser,topic,note):
        msg = EmailMessage()
        msg['Subject'] = f'Kasta VA: Note - {topic}'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = emailUser

        username = firstName
        email = emailUser


        file_loader = FileSystemLoader('EmailService/templates')
        env = Environment(loader=file_loader)
        template = env.get_template('note.html')
        output = template.render(email=email, username=username, topic=topic, note=note)
        msg.add_alternative(output, subtype='html')

        self.smtpObj.send_message(msg)

