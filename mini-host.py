import time, serial, sys # provide a serial port on the command line
serial.Serial(sys.argv[1], baudrate=115200).write(
    str(list(time.localtime())).encode() + b"\r\n"
)
