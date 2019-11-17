class Time:
    def __init__(self):
        self.hour = 0
        self.minute = 0
        self.second = 0
        self.AmPm = 'A.M'
        self.APnum = 0

    def second_append(self):
        while True:
            self.second += 1
            sleep(1)
            if self.second >= 60:
                self.MinuteAppend(1)
                self.second = 0

    def minute_append(self, min):
        self.minute += min
        if self.minute >= 60:
            self.hour_append(int(self.minute / 60))
            self.minute %= 60

    def hour_append(self, hr):
        if n == 0:
            return None
        self.hour += 1
        if self.hour == 12:
            self.hour = 0
            ap_list = ['A.M', 'P.M']
            ap_list.remove(self.AmPm)
            self.AmPm = ap_list[0]
            if self.AmPm == 'A.M':
                print('Day 1 passed')
                sleep(3)
        self.hour_append(hr - 1)

    def show_time(self):
        print('%02d : %02d : %02d' % (self.hour, self.minute, self.second))
