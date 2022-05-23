from machine import Pin

# create an output pin on pin #0
p0 = Pin(17, Pin.OUT)
led = Pin(25,Pin.OUT)
# set the value low then high
led.on()
p0.value(1)