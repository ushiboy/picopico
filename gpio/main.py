from machine import Pin
import time
import _thread

led = Pin(16, Pin.OUT)

def pressed(pin):
    print("pressed")
    print(pin.irq().flags())

btn = Pin(17, Pin.IN)
btn.irq(pressed, Pin.IRQ_FALLING)

def th1():
    while True:
        led.value(1 if led.value() == 0 else 0)
        time.sleep(2)

_thread.start_new_thread(th1, ())
