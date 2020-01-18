from microbit import *
from random import *

while True:
    if button_a.is_pressed():
        display.clear()
        
    gesture = accelerometer.current_gesture()
    if gesture == "freefall":
        a=random(1,9)
        display.show(a)
        