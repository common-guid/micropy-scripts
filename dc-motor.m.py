## pi pico with tb6612 sparkfun driver
## test script
    # pwm duty controls speed
    # stby needs be on/high to run
    # voltage controls motor potential

from machine import PWM, Pin
from time import sleep_ms

stby = Pin(21, Pin.OUT)
a1 = Pin(19,Pin.OUT)
a2 = Pin(18,Pin.OUT)
pwm = PWM(Pin(17,Pin.OUT))
led = Pin(25,Pin.OUT)
led.on()
stby.on()

for i in range(500, 10000, 500):
    pwm.duty_u16(i)
    a1.off()
    a2.on()
    print(i)
    sleep_ms(500)
led.off()