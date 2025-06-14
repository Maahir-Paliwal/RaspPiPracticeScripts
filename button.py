#to discover button functionality

from gpiozero import Button
from signal import pause

button = Button(26, pull_up = True, hold_time=5.0)

def hello():
    print("I am a button")


def held():
    print("I am being held")


#give it the function id
button.when_pressed = hello
button.when_held = held

pause()
