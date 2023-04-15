"""
TODO: don't use json, parse simpler for M0 compat
- Default to usb_cdc.data if available
- Use USB CDC if available
- Use sys.stdin/print as last resort
- Force by passing a channel
- Accept UART channels, anything that has a read and write
"""
import busio
import json
import rtc
import supervisor
import sys
import time

the_rtc = rtc.RTC()

class HostAccess:
    def __init__(self, channel=None, verbose=False):
        self.read_if_available = None
        self.write = None
        self.channel = channel

        if self.channel is None:
            try:
                import usb_cdc
                if usb_cdc.data:
                    self.channel = usb_cdc.data
                else:
                    self.channel = usb_cdc.console
            except ImportError:
                pass

        if self.channel is None:
            self.channel = sys.stdin
            self.read_if_available = self.stdin_read
            self.write = self.stdout_write

        # USB CDC or UART
        if hasattr(self.channel, "in_waiting"):
            self.read_if_available = self.stream_read
            self.write = self.stream_write

        if self.read_if_available is None:
            self.read_if_available = self.default_read
        if self.write is None:
            self.write = self.default_write

    def stream_read(self):
        if nbytes := self.channel.in_waiting:
            return self.channel.read(nbytes)
        return ""
    def stream_write(self, data):
        channel.write(data)

    def stdin_read(self):
        buffer = ""
        while supervisor.runtime.serial_bytes_available:
            buffer += sys.stdin.read(1)
        return buffer.encode()

    def stdout_write(data):
        print(data.decode())

    def default_read(self):
        return self.channel.read()

    def default_write(self, data):
        self.channel.write(data)

class TimeReader(HostAccess):
    def poll():
        # data format: (2023, 3, 20, 1, 0, 0, 0, 0, 0)
        if data := self.read_if_available():
            if data.endswith(b"\n"):
                data = data.strip()
                try:
                    timestamp = json.loads(data)
                    the_rtc.datetime = time.struct_time(timestamp)
                    if verbose: print(f"Time set to {timestamp}")
                except ValueError as er:
                    if verbose: print(er)
                    if verbose: print(data)

if __name__ == "__main__":
    time_reader = TimeReader(verbose=True)
    while True:
        time_reader.poll()
        print("Doing other stuff")
        time.sleep(1)
