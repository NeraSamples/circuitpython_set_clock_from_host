import time
import json
import rtc

the_rtc = rtc.RTC()

while True:
    data = input()
    try:
        timestamp = json.loads(data)
        the_rtc.datetime = time.struct_time(timestamp)
    except Exception as er:
        print("skip", time.localtime())
