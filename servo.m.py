import time
from machine import Pin
from machine import PWM
pwm = PWM(Pin(20))
pwm.freq(50)
#for i in range(1000, 5000, 1000):
 #   pwm.duty_u16(i)
  #  sleep(2)
   # print(i)

while True:
    pwm.duty_u16(2500)
    time.sleep_ms(100)
    pwm.duty_u16(0)
    time.sleep(5)