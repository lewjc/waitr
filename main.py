from gpiozero import Button, LED
from time import sleep
from playsound import playsound

button = Button(2)
led = LED(4)

led.toggle()

try:
    while True:
        if button.is_pressed:
            led.off()
            playsound('./sound.mp3')
            led.on()
        else:
            sleep(0.2)
except:
    pass