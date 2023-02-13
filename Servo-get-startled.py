#repositories (dont delete 'em)
from machine import Pin # get the pins
from time import sleep # sleep so it can wait
from board manager import D4 # THE PIN
from robot_manager import Servo # and the servo stuff

class Servo_Spray (Servo):
   def _init_(self, pin, rest=100, press=0, wait=0.3):
     from time import sleep
     self.s = super().init _(pin)
     self.rest = rest
     self.press = press
     self.wait = wait
     
   def spray (self):
     self.write_angle(self.press)
     sleep(self.wait)
     servo.write_angle(self.rest)
     
servo = Servo_Spray (D4, 100, 0, 0.2)
sleep (0.3)
print("Turning servo")
servo.spray()
