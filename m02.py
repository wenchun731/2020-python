# Add your Python code here. E.g.
from microbit import *


while True:
    if button_a.is_pressed():
        display.show('a')
   
    if button_b.is_pressed():
        display.show('b')
        
    if button_a.is_pressed() and button_b.is_pressed():
        display.show(Image.HAPPY)
        sleep(2000)
   
   
    
    