# circuitpython_set_clock_from_host
Script to set clocks from the host PC, manually one time or as a background for an application.

## Data port

To use the data port instead of the REPL port, create a boot.py file with:
```py
import usb_cdc
usb_cdc.enable(data=True)
```

And reset the board. ([See more in the USB serial guide](https://github.com/NeraSamples/circuitpython_usb_serial#the-second-serial-channel)).
