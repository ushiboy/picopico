from machine import Pin

led = Pin(16, Pin.OUT)

def pressed(pin):
    led.toggle()

btn = Pin(17, Pin.IN)
btn.irq(pressed, Pin.IRQ_FALLING)
