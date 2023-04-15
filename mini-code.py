import time, json, rtc
while True:rtc.RTC().datetime = time.struct_time(json.loads(input()))
