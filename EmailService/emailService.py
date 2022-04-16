from emailConfig import EMAIL_ADDRESS
from emailConfig import EMAIL_PASSWORD
import smtplib
from email.message import EmailMessage
import codecs

msg = EmailMessage()
msg['Subject'] = 'Grab dinner'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'niecko.jakub@gmail.com'

htmlFile = codecs.open('hello.html', 'r', 'utf-8')
text = htmlFile.read()
msg.add_alternative(text, subtype='html')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    smtp.send_message(msg)