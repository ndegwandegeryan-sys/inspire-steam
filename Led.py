#Name : ndegwandegeryan
#Date : 13/02/2026
#program to blink leds


from machine import Pin 
import time

red_led = Pin(28, Pin.OUT)
yellow_led=Pin(27,Pin.OUT)
while True:
  red_led.on()
  yellow_led.off()
  time.sleep(1) # Wait for USB to become ready
  print("Learning IOT")
  red_led.off()
  yellow_led.on()
  time.sleep(2)
  print("This is yellow")