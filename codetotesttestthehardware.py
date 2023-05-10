# Hardware Test
# Blink and LED (GP15) slowly/quickly while a button (GP16) is not-pressed/pressed
from machine import Pin
from time import sleep_ms

led = Pin(2, Pin.OUT) #2 is the pin in which the LED is connected and 12 is the standard pin in which button A is connected in Pico Explorer
button = Pin(12, Pin.IN, Pin.PULL_UP)

while True:
    if button.value() == 0: # button pressed
        delay = 100 # short delay
    else:
        delay = 1000 # long delay
    
    led.toggle()
    sleep_ms(delay)
