from datetime import datetime


class SystemInfo:
    def __init__(self):
        pass

    @staticmethod
    def get_time():
        now = datetime.now()
        answer = "The time is {} {}".format(now.hour, now.minute)
        return answer
