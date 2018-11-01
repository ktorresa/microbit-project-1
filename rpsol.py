# Add your Python code here. E.g.
from microbit import *
import random

scissor = Image("99009:"
                "99090:"
                "09900:"
                "99090:"
                "99009:")


rock = Image(   "0000:"
                "09990:"
                "09990:"
                "09990:"
                "00000:")


paper = Image(  "99999:"
                "99999:"
                "99999:"
                "99999:"
                "99999:")


lizard = Image( "00900:"
                "09990:"
                "00900:"
                "09990:"
                "00900:")


spock = Image(  "90009:"
                "90009:"
                "99099:"
                "09990:"
                "00900:")


while True:
    if accelerometer.was_gesture("shake"):
        display.clear()
    
        hand = random.randint(0, 4)
        if hand == 0:
           display.show(scissor)
           
            
        elif hand == 1:
            display.show(rock)
           
            
           
        elif hand == 2:
            display.show(paper)
            
            
        elif hand == 3:
            display.show(lizard)
            
            
        else:
            display.show(spock)
            
            
            
        

        

