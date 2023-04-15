import time
import serial
import sys

BOARD_UID = ""

if len(sys.argv) == 2:
    device = sys.argv[1]
else:
    import adafruit_board_toolkit.circuitpython_serial
    comports = []
    comports = adafruit_board_toolkit.circuitpython_serial.data_comports()
    if not comports:
        comports = adafruit_board_toolkit.circuitpython_serial.repl_comports()

    if BOARD_UID:
        for port in comports:
            device = port.device
            if port.serial_number == BOARD_UID:
                break
    else:
        device = comports[0].device

print(device)

with serial.Serial(device, timeout=5, baudrate=115200) as channel:
    timestamp = str(list(time.localtime())).encode()
    channel.write(timestamp + b"\r\n")
    data = channel.readline()
    if data.startswith(b"Time set to"):
        print("ok")
        print(data.decode())
    else:
        print("error ?")
        print(data)
