from twilio.rest import Client
from SMSService.serviceConfig import account_ssid
from SMSService.serviceConfig import auth_token
from SMSService.serviceConfig import number


client = Client(account_ssid, auth_token)


class SendSms():

    def __init__(self):
        client = Client(account_ssid, auth_token)


    def send_reminder(self,reminder,date,user_phone_number):
        reminder_message = f"This is your KASTA VA Reminder! \nReminder: {reminder} \nDate: {date}"
        message = client.messages.create(body=reminder_message, from_ = number, to=user_phone_number)

    def send_note(self, topic, description, user_phone_number):
        note_message = f"This is your KASTA VA Note: \nTopic: {topic} \nDescription: {description}"
        message = client.messages.create(body=note_message, from_=number, to=user_phone_number)


