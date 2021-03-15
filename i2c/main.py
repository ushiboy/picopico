from machine import Pin, I2C
import time

i2c = I2C(0, scl=Pin(21), sda=Pin(20))
print(i2c.scan())
