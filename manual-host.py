import time
import serial
import sys

# provide a serial port on the command line
device = sys.argv[1]

with serial.Serial(device, baudrate=115200) as channel:
    timestamp = str(list(time.localtime())).encode()
    channel.write(timestamp + b"\r\n")
