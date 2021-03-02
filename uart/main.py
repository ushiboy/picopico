from machine import UART
import time

uart = UART(0, 115200)
uart.write('abc\n')

while True:
    buf = b''
    while uart.any() > 0:
        buf += uart.read(1)
    if len(buf) > 0:
        print(buf)
        #uart.write(buf)
    time.sleep(1)
