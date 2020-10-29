import time
import datetime

class TimeHandler:

    @staticmethod
    def current_time():
        dt = datetime.datetime.now()
        return int(time.mktime(dt.timetuple()))

    @staticmethod
    def string_toTimestamp(timestr):
        return int(time.mktime(time.strptime(timestr,"%Y-%m-%d %H:%M:%S")))

if __name__ == '__main__':
    print(TimeHandler().current_time())
    print(TimeHandler().string_toTimestamp('2020-10-27 11:11:11'))