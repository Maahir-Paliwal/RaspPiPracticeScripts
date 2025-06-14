#to discover button functionality

from gpiozero import Button
from signal import pause

button = Button(26, pull_up = True)

def hello():
    print("I am a button")

#give it the function id
button.when_pressed = hello

pause()
