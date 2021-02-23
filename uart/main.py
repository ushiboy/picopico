from machine import UART

uart = UART(0, 115200)
uart.write('abc\n')
