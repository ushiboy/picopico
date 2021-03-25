from machine import Pin, I2C
import time

i2c = I2C(0, scl=Pin(21), sda=Pin(20))
addr = i2c.scan()[0]

WRITE_COMMAND = 0x00
WRITE_DATA = 0x40

i2c.writeto_mem(addr, WRITE_COMMAND, b'\x38')
i2c.writeto_mem(addr, WRITE_COMMAND, b'\x39')
i2c.writeto_mem(addr, WRITE_COMMAND, b'\x14')
i2c.writeto_mem(addr, WRITE_COMMAND, b'\x73')
i2c.writeto_mem(addr, WRITE_COMMAND, b'\x56')
i2c.writeto_mem(addr, WRITE_COMMAND, b'\x6c')
time.sleep(0.2)
i2c.writeto_mem(addr, WRITE_COMMAND, b'\x02')
time.sleep(0.2)
i2c.writeto_mem(addr, WRITE_COMMAND, b'\x01')
time.sleep(0.2)
i2c.writeto_mem(addr, WRITE_COMMAND, b'\x0f')
time.sleep(0.2)

i2c.writeto_mem(addr, WRITE_COMMAND, b'\x38')
i2c.writeto_mem(addr, WRITE_DATA, bytes([ord('A')]))
i2c.writeto_mem(addr, WRITE_DATA, bytes([ord('B')]))
i2c.writeto_mem(addr, WRITE_DATA, bytes([ord('C')]))
