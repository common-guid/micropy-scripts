from machine import Pin, PWM

m1 = Pin(20, Pin.OUT)
m2 = Pin(21, Pin.OUT)
stby = Pin(16, Pin.OUT)
pwma = PWM(Pin(18, Pin.OUT))
pwma.duty_u16(16000)
print(pwma.duty_ns())

stby.high()
m1.high()
m2.low()