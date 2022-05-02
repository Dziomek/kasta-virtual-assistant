from plyer import notification


def notify_me(text):
    message = text.split('notification', 2)[1]
    notification.notify(title='Kasta notification', message=message, app_icon='icons/not_icon.ico')
