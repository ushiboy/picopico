from machine import Pin
from onewire import OneWire
from ds18x20 import DS18X20
import time

ds = Pin(16, Pin.OUT)
sensor = DS18X20(OneWire(ds))

roms = sensor.scan()

while True:
    sensor.convert_temp()
    time.sleep_ms(750)
    for rom in roms:
        print(sensor.read_temp(rom))
    time.sleep(2)
