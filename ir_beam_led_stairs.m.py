# ir beams + relay + led rope lights
# GP 18 = ir beam out [NO]
# GP 21 = relay sig
 
from machine import Pin
import time

beam = Pin(18, Pin.IN, Pin.PULL_DOWN)
sig = Pin(21, Pin.OUT)
led = Pin(25, Pin.OUT)

led.off()
while True:
    if beam.value() == 1:
        sig.on()
        led.off()
        time.sleep(30.0)
        sig.off()
    time.sleep(1.0)
