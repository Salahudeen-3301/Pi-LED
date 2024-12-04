from gpiozero import LED, Button
from time import sleep
led = LED(23)
button = Button(24)
while True:
    if button.is_active:
        led.on()
    else:
        led.off()
