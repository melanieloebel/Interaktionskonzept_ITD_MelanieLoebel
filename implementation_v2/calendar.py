import datetime

class Calendar:
    def __init__(self):
        self.morning = self.create_morning_times()
        self.afternoon = self.create_afternoon_times()

    def create_morning_times(self):
        return [
            datetime.time(8, 00),
            datetime.time(8, 30),
            datetime.time(9, 00),
            datetime.time(9, 30),
            datetime.time(10, 00),
            datetime.time(10, 30),
            datetime.time(11, 00),
            datetime.time(11, 30),
            datetime.time(12, 00),
            datetime.time(12, 30)
        ]

    def create_afternoon_times(self):
        return [
            datetime.time(13, 00),
            datetime.time(13, 30),
            datetime.time(14, 00),
            datetime.time(14, 30),
            datetime.time(15, 00),
            datetime.time(15, 30),
            datetime.time(16, 00),
            datetime.time(17, 00),
            datetime.time(16, 30),
            datetime.time(17, 30)
        ]
